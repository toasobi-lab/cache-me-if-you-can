# 🚀 Cache Me If You Can

A comprehensive, production-ready microservice project designed to teach Redis caching patterns through hands-on experience. Features FastAPI backend, PostgreSQL database, Redis cache, and an interactive Astro frontend with **real-time performance metrics**.

Perfect for learning cache-aside patterns, Docker orchestration, and microservice architecture in a realistic development environment.

![Main Interface](docs/screenshots/main-interface.png)
*The main testing interface with real-time performance metrics and cache statistics*

## 🔧 Tech Stack

| Component     | Tool/Framework    | Version | Purpose                           |
|---------------|-------------------|---------|-----------------------------------|
| Backend       | FastAPI + Uvicorn | Python 3.12.3 | RESTful API service               |
| Database      | PostgreSQL        | 15.6    | Primary data store                |
| Cache         | Redis             | 7.2.5   | High-performance caching layer    |
| Frontend      | Astro + Tailwind  | Node 20.12.0 | Interactive testing interface     |
| DB Admin      | pgAdmin           | 9.4     | PostgreSQL management UI          |
| Cache Admin   | Redis Commander   | Latest  | Redis visualization & management  |
| Orchestration | Docker Compose    | Latest  | Service coordination              |

## 🏗️ Architecture

```ascii
┌──────────────────┐   GET /products/{id}   ┌──────────────────┐
│                  │──────────────────────→│                  │
│  Astro Frontend  │                        │  FastAPI Backend │
│ (localhost:3000) │←──────────────────────│ (localhost:8000) │
│                  │  4. JSON + Metrics     │                  │
└──────────────────┘                        └─────────┬────────┘
                                                      │
                                                      │ 1. Check Redis
                                                      │
                                            ┌─────────▼─────────┐
                                            │                   │
                                            │    Redis Cache    │
                                            │ (localhost:6379)  │
                                            └─────────┬─────────┘
                                                      │
                                          ┌───────────┴───────────┐
                                          │                       │
                                     ✅ Cache Hit           ❌ Cache Miss
                                          │                       │
                               (2ms response)                     │
                                                                  ▼
                                                     ┌─────────────────────┐
                                                     │                     │
                                                     │ PostgreSQL Database │
                                                     │  (localhost:5432)   │
                                                     └──────────┬──────────┘
                                                                │
                                                                │ 2. Query DB
                                                                │ (50-200ms)
                                                                │
                                                     3. Cache result & return
```

## 🚀 Quick Start

### Prerequisites
- **Docker** (20.10+) and **Docker Compose** (2.0+) installed
- Available ports: `3000`, `8000`, `5432`, `6379`, `5050`, `5540`
- At least 2GB RAM available for containers

### 1. Launch All Services
```bash
# Start all services (first run will build images)
docker compose up -d --build

# Check all services are healthy
docker compose ps
```

### 2. Access Applications

| Service | URL | Credentials | Purpose |
|---------|-----|-------------|---------|
| **Frontend** | http://localhost:3000 | None | Main testing interface |
| **API Docs** | http://localhost:8000/docs | None | Interactive API documentation |
| **pgAdmin** | http://localhost:5050 | `admin@cacheme.com` / `admin123` | Database management |
| **Redis Commander** | http://localhost:5540 | None | Cache visualization |

![Redis Commander](docs/screenshots/redis-commander.png)
*Redis Commander interface showing cached product keys, data types, and TTL information*

![pgAdmin Interface](docs/screenshots/pgadmin-interface.png)
*pgAdmin automatically configured with PostgreSQL connection and sample product data*

### 3. Automated Setup
🎉 **Everything is pre-configured!** 
- PostgreSQL initializes with 15 sample products
- pgAdmin automatically connects to the database
- Redis Commander connects to the cache
- No manual configuration required!

## 🔴 Understanding Redis Caching

### What is Redis?
**Redis** (Remote Dictionary Server) is an in-memory data structure store that serves as a database, cache, and message broker. It's one of the most popular caching solutions used by companies like Twitter, GitHub, Instagram, and Snapchat.

### 🚨 Problems Redis Solves

#### **The Database Bottleneck Problem**
- **Traditional Issue**: Every user request hits the database directly
- **Result**: Slow response times, high server costs, poor user experience
- **Redis Solution**: Cache frequently accessed data in memory for instant retrieval

#### **Real-World Scenarios:**
- **E-commerce**: Product catalogs, user sessions, shopping carts
- **Social Media**: User profiles, news feeds, trending content
- **Gaming**: Leaderboards, player stats, game state
- **Financial**: Stock prices, exchange rates, account balances
- **Content Delivery**: Web pages, API responses, search results

### 🏢 Popular Use Cases

#### **1. Database Query Caching**
```
Before: Database query takes 200ms
After: Redis cache hit takes 2ms (100x faster!)
```

#### **2. Session Storage**
- Store user login sessions across multiple servers
- Enable seamless user experience in distributed systems
- Automatic session expiration with TTL

#### **3. Real-Time Analytics**
- Count page views, user actions, API calls
- Track trending topics and popular content
- Generate dashboards with live metrics

#### **4. Rate Limiting**
- Prevent API abuse by tracking request counts
- Implement "try again later" functionality
- Protect services from overload

#### **5. Pub/Sub Messaging**
- Real-time notifications and chat systems
- Microservice communication
- Live updates and event streaming

### ⚡ Key Redis Advantages:
- **🚀 Speed**: In-memory storage = microsecond response times
- **🗂️ Data Structures**: Strings, hashes, lists, sets, sorted sets, bitmaps
- **⏰ Smart Expiration**: Automatic data cleanup with TTL
- **🔄 Persistence**: Optional disk backup for data safety
- **📊 Monitoring**: Built-in statistics and performance metrics
- **🔧 Atomic Operations**: Thread-safe operations for concurrent access

### 🔄 Cache-Aside Pattern (Our Implementation):
1. **Application Request**: User wants product data
2. **Check Cache First**: Query Redis for cached product
3. **Cache Miss**: If not found, query PostgreSQL database
4. **Cache Population**: Store database result in Redis with TTL
5. **Cache Hit**: Next request gets data instantly from Redis
6. **Performance Win**: 10-100x faster response for subsequent requests

### 💰 Business Impact:
- **Performance**: Sub-millisecond response times
- **Scalability**: Handle 10x more users with same infrastructure
- **Cost Savings**: Reduce database server requirements by 50-80%
- **User Experience**: Faster page loads = higher conversion rates
- **Reliability**: Less database load = fewer timeouts and errors

## ⚡ Performance Comparison

> **💡 Local Environment Note**: The screenshots below show results from a local development environment. Your actual response times may vary based on system resources, but you'll always observe the same dramatic performance difference between cache hits and database queries.

### Cache Hit (Fast) ⚡
![Redis Cache Speed](docs/screenshots/redis-speed.png)
*Redis cache hit - served directly from memory for maximum speed*

### Cache Miss (Slower) 🐢
![Database Query Speed](docs/screenshots/db-speed.png)
*PostgreSQL database query - requires disk I/O and processing time*

### Performance Expectations
| Scenario | Response Time | Source | Notes |
|----------|---------------|---------|-------|
| Cache Hit | ~2-15ms | Redis | Varies by system |
| Cache Miss | ~20-300ms | PostgreSQL | Varies by system |
| **Speed Improvement** | **5-50x faster** | Cache vs DB | **The key is the relative difference!** |

> **💡 Performance Note**: Actual response times vary based on your system (CPU, RAM, Docker resources, etc.), but you'll always see cache hits being significantly faster than database queries. The learning value is in observing this performance difference, not the absolute numbers.

## 🧪 Interactive Features

### Testing Dashboard
- **Product Lookup**: Test individual products with real-time metrics
- **Quick Test Buttons**: One-click testing for products 1, 5, and 10
- **Performance Tracking**: Visual indicators for cache vs database responses
- **Cache Management**: Clear all cached data with one button

### Real-Time Metrics
- **Response Time Tracking**: See exact millisecond differences
- **Source Identification**: Know if data came from cache or database
- **Visual Indicators**: Color-coded responses (green=cache, blue=database)
- **Live Statistics**: Watch cache performance improve over time

## 📊 Cache Statistics Dashboard

![Cache Statistics](docs/screenshots/cache-stats.png)
*Live Redis cache statistics dashboard showing all the key metrics explained below*

### Key Performance Indicators
- **Cache Hits**: Successful cache retrievals (fast responses)
- **Cache Misses**: Cache lookups that required database queries
- **Hit Rate**: `(Hits / (Hits + Misses)) × 100` - Higher is better!
- **Memory Usage**: Current Redis memory consumption
- **Connected Clients**: Active connections (typically 2: backend + Redis Commander)
- **Total Commands**: All Redis operations since startup (GET, SET, INFO, PING, etc.) - shows overall Redis activity

### What Good Performance Looks Like:
- **Hit Rate**: 80%+ in production applications
- **Memory Usage**: Stable, not constantly growing
- **Response Times**: Consistent cache hit speeds

## 🔧 API Reference

### Core Endpoints
```http
GET    /products/{id}     # Get product with caching & metrics
GET    /products          # List all products (paginated)
GET    /cache/stats       # Redis cache statistics  
DELETE /cache/clear       # Clear all cached data
GET    /health            # Service health check
```

### Response Format
All product endpoints include performance metrics:
```json
{
  "id": 1,
  "name": "Wireless Headphones",
  "category": "Electronics", 
  "price": 79.99,
  "description": "High-quality wireless headphones...",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00",
  "source": "cache",           // "cache" or "database"
  "fetch_time_ms": 2.45        // Processing time in milliseconds
}
```

### Cache Statistics Response
```json
{
  "cache_stats": {
    "keyspace_hits": 42,
    "keyspace_misses": 8, 
    "used_memory_human": "1.2M",
    "connected_clients": 2,
    "total_commands_processed": 156
  }
}
```

## 🛠️ Volume Management

### Named Volumes
All data is stored in clearly named volumes for easy management:

```bash
# List all project volumes
docker volume ls | grep cache-me

# Volume purposes:
# cache-me-postgres-data        → Database files
# cache-me-redis-data          → Cache persistence  
# cache-me-pgadmin-data        → Admin configuration
# cache-me-frontend-node-modules → Dependencies
```

### Data Management Commands
```bash
# View volume details
docker volume inspect cache-me-postgres-data

# Complete reset (removes all data)
docker compose down -v

# Backup database volume
docker run --rm -v cache-me-postgres-data:/data -v $(pwd):/backup ubuntu tar czf /backup/postgres-backup.tar.gz /data
```

## 🐛 Troubleshooting

### Common Issues

**🔴 Services won't start**
```bash
# Check port conflicts
netstat -tulpn | grep -E ':(3000|8000|5432|6379|5050|5540)'

# View service logs
docker compose logs <service-name>
```

**🔴 Database connection issues**
```bash
# Reset database volume
docker compose down
docker volume rm cache-me-postgres-data
docker compose up -d
```

**🔴 Cache not working**
```bash
# Check Redis connectivity
docker compose exec backend redis-cli -h redis ping

# View backend logs
docker compose logs -f backend
```

**🔴 pgAdmin server not auto-configured**
```bash
# Reset pgAdmin configuration
docker compose down
docker volume rm cache-me-pgadmin-data
docker compose up -d
```

### Performance Issues
- **Slow responses**: Check Docker resource allocation (increase RAM/CPU)
- **High memory usage**: Clear cache via UI or restart Redis container
- **Connection timeouts**: Ensure all services are healthy: `docker compose ps`

### Complete Reset
```bash
# Nuclear option - removes everything
docker compose down -v --remove-orphans
docker system prune -f
docker compose up -d --build
```

## 🔍 Monitoring & Logs

### Real-time Monitoring
```bash
# Follow all service logs
docker compose logs -f

# Monitor specific service
docker compose logs -f backend

# Watch cache operations
docker compose logs -f backend | grep -i cache
```

### Health Checks
```bash
# Check service health
docker compose ps

# Test API health
curl http://localhost:8000/health

# Test cache connectivity  
curl http://localhost:8000/cache/stats
```

## 🎓 Learning Path

### Beginner
1. **Start services** and explore the frontend
2. **Test cache behavior** with the same product ID multiple times
3. **Monitor statistics** to see hit rates improve
4. **Clear cache** and observe the reset

### Intermediate  
5. **Examine logs** to understand cache-aside pattern
6. **Explore Redis Commander** to see cached keys
7. **Check pgAdmin** to understand the source data
8. **Modify TTL** in the backend code and observe behavior

### Advanced
9. **Scale services** with `docker compose up --scale backend=3`
10. **Implement cache warming** strategies
11. **Add monitoring** with Prometheus/Grafana
12. **Benchmark performance** under load

## 🤝 Contributing

This project is designed for learning. Feel free to:
- Add new caching strategies
- Implement additional metrics
- Enhance the frontend UI
- Add monitoring tools
- Create performance benchmarks

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

MIT License - Feel free to use this project for learning and teaching purposes.