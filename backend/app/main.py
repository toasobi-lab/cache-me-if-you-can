from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import logging
import time

from .db import get_db, engine
from .models import Base, Product, ProductResponse
from .cache import get_from_cache, set_in_cache, get_cache_stats, clear_all_cache

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cache Me If You Can - Product API",
    description="A microservice demonstrating Redis caching with FastAPI and PostgreSQL",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Cache Me If You Can - Product API",
        "version": "1.0.0",
        "endpoints": {
            "get_product": "/products/{id}",
            "cache_stats": "/cache/stats",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}

@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get a product by ID with Redis caching.
    First checks Redis cache, then falls back to PostgreSQL.
    """
    start_time = time.perf_counter()
    logger.debug(f"Received request for product_id: {product_id}")
    cache_key = f"product:{product_id}"
    
    # Try to get from cache first
    cached_product = get_from_cache(cache_key)
    if cached_product:
        logger.debug(f"Returning cached product: {product_id}")
        end_time = time.perf_counter()
        cached_product['source'] = 'cache'
        cached_product['fetch_time_ms'] = (end_time - start_time) * 1000
        return ProductResponse(**cached_product)
    
    # Cache miss - query database
    logger.info(f"Cache miss for product {product_id}, querying database...")
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        logger.warning(f"Product with id: {product_id} not found in database.")
        raise HTTPException(status_code=404, detail="Product not found")
    
    logger.debug(f"Found product {product_id} in database. Preparing to cache.")
    # Convert to dict for caching
    product_dict = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "category": product.category,
        "created_at": str(product.created_at) if product.created_at else None,
        "updated_at": str(product.updated_at) if product.updated_at else None
    }
    
    # Cache the result for 1 hour
    set_in_cache(cache_key, product_dict, ttl=3600)
    
    logger.debug(f"Returning product {product_id} from database.")
    
    end_time = time.perf_counter()
    product_dict['source'] = 'database'
    product_dict['fetch_time_ms'] = (end_time - start_time) * 1000
    
    return ProductResponse(**product_dict)

@app.get("/cache/stats")
async def get_cache_statistics():
    """Get Redis cache statistics"""
    stats = get_cache_stats()
    return {
        "cache_stats": stats,
        "timestamp": time.time()
    }

@app.delete("/cache/clear")
async def clear_cache_endpoint():
    """Clear all cached data"""
    try:
        cleared_count = clear_all_cache()
        return {
            "message": "Cache cleared successfully",
            "cleared_keys": cleared_count,
            "timestamp": time.time()
        }
    except Exception as e:
        logger.error(f"Failed to clear cache: {e}")
        raise HTTPException(status_code=500, detail="Failed to clear cache")

@app.get("/products")
async def list_products(db: Session = Depends(get_db), limit: int = 10):
    """List all products (limited for demo purposes)"""
    products = db.query(Product).limit(limit).all()
    return [
        ProductResponse(
            id=p.id,
            name=p.name,
            description=p.description,
            price=p.price,
            category=p.category,
            created_at=str(p.created_at) if p.created_at else None,
            updated_at=str(p.updated_at) if p.updated_at else None
        ) for p in products
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 