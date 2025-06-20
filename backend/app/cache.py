import redis
import json
import os
from typing import Optional, Any
import logging

logger = logging.getLogger(__name__)

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")

# Create Redis connection
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

def get_from_cache(key: str) -> Optional[dict]:
    """Get data from Redis cache"""
    try:
        data = redis_client.get(key)
        if data:
            logger.info(f"Cache HIT for key: {key}")
            return json.loads(data)
        logger.info(f"Cache MISS for key: {key}")
        return None
    except Exception as e:
        logger.error(f"Error getting from cache: {e}")
        return None

def set_in_cache(key: str, value: Any, ttl: int = 3600) -> bool:
    """Set data in Redis cache with TTL (default 1 hour)"""
    try:
        serialized_value = json.dumps(value, default=str)
        redis_client.setex(key, ttl, serialized_value)
        logger.info(f"Data cached with key: {key}, TTL: {ttl}s")
        return True
    except Exception as e:
        logger.error(f"Error setting cache: {e}")
        return False

def delete_from_cache(key: str) -> bool:
    """Delete data from Redis cache"""
    try:
        result = redis_client.delete(key)
        logger.info(f"Cache key deleted: {key}")
        return result > 0
    except Exception as e:
        logger.error(f"Error deleting from cache: {e}")
        return False

def clear_all_cache() -> int:
    """Clear all cached data and return the number of keys deleted"""
    try:
        # Get all keys matching our product pattern
        product_keys = redis_client.keys("product:*")
        if product_keys:
            deleted_count = redis_client.delete(*product_keys)
            logger.info(f"Cleared {deleted_count} cache keys")
            return deleted_count
        logger.info("No cache keys to clear")
        return 0
    except Exception as e:
        logger.error(f"Error clearing cache: {e}")
        return 0

def get_cache_stats() -> dict:
    """Get Redis cache statistics"""
    try:
        info = redis_client.info()
        return {
            "total_connections_received": info.get("total_connections_received", 0),
            "total_commands_processed": info.get("total_commands_processed", 0),
            "keyspace_hits": info.get("keyspace_hits", 0),
            "keyspace_misses": info.get("keyspace_misses", 0),
            "used_memory_human": info.get("used_memory_human", "0B"),
            "connected_clients": info.get("connected_clients", 0)
        }
    except Exception as e:
        logger.error(f"Error getting cache stats: {e}")
        return {} 