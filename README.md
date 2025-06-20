# 🚀 Cache Me If You Can

A comprehensive, production-ready microservice project designed to teach Redis caching patterns through hands-on experience. Features FastAPI backend, PostgreSQL database, Redis cache, and an interactive Astro frontend with **real-time performance metrics**.

Perfect for learning cache-aside patterns, Docker orchestration, and microservice architecture in a realistic development environment.

## 🔧 Tech Stack

| Component     | Tool/Framework    | Version | Purpose                           |
|---------------|-------------------|---------|-----------------------------------|
| Backend       | FastAPI + Uvicorn | Latest  | RESTful API service               |
| Database      | PostgreSQL        | 15.6    | Primary data store                |
| Cache         | Redis             | 7.2.5   | High-performance caching layer    |
| Frontend      | Astro + Tailwind  | Latest  | Interactive testing interface     |
| DB Admin      | pgAdmin           | 9.4     | PostgreSQL management UI          |
| Cache Admin   | Redis Commander   | Latest  | Redis visualization & management  |
| Orchestration | Docker Compose    | Latest  | Service coordination              |

## 🏗️ Architecture

```ascii
+------------------+   GET /products/{id}   +------------------+
|                  |----------------------->|                  |
|  Astro Frontend  |                        |  FastAPI Backend |
| (localhost:3000) |<-----------------------| (localhost:8000) |
|                  |  4. Return JSON Data   |                  |
+------------------+                        +--------+---------+
                                                     |
                                                     | 1. Check for key in Redis
                                                     |
                                           +---------v---------+
                                           |                   |
                                           |    Redis Cache    |
                                           +-------------------+
                                                     |
                                          +----------+----------+
                                          |                     |
                                     ✅ Cache Hit           ❌ Cache Miss
                                          |                     |
                               (Return to Backend)              v
                                                     +-----------------------+
                                                     |                       |
                                                     |  PostgreSQL Database  |
                                                     +----------+------------+
                                                                |
                                                                | 2. Query Database
                                                                |
                                                     (Return to Backend)
                                                                |
                                                                | 3. Store in Redis
                                                                v
                                                         (Return to Backend)
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

### 3. Automated Setup
🎉 **Everything is pre-configured!** 
- PostgreSQL initializes with 15 sample products
- pgAdmin automatically connects to the database
- Redis Commander connects to the cache
- No manual configuration required!

## 🎯 Learning Objectives & Features

### 🏃‍♂️ **Real-Time Performance Comparison**
Experience the dramatic speed difference between cache hits and database queries:

**First Request (Cache Miss):**
- 🔵 Shows "Database (Slow)" in blue
- ⏱️ Typical response: 50-200ms
- 📊 Increments cache miss counter

**Subsequent Requests (Cache Hit):**
- 🟢 Shows "Cache (Fast)" in green  
- ⚡ Typical response: 1-10ms (10-100x faster!)
- 📈 Increments cache hit counter

### 🧪 **Interactive Testing Features**
- **Product Lookup**: Test individual products with real-time metrics
- **Quick Test Buttons**: One-click testing for products 1, 5, and 10
- **Cache Statistics**: Live Redis metrics (hits, misses, hit rate, memory usage)
- **Cache Management**: Clear all cached data with one button
- **Performance Tracking**: Visual indicators for cache vs database responses

### 🔍 **Understanding Sidecar Caching**
- **Cache-First Strategy**: The application always checks Redis first before hitting the database.
- **Automatic Population**: On cache misses, data is automatically stored in Redis for future requests.
- **TTL Management**: Cached data expires after 1 hour to ensure freshness.

### 📊 **Monitoring Cache Performance**
Watch the application logs to see cache behavior in real-time:
```bash
docker compose logs -f backend
```

You'll see messages like:
- `"Cache miss for product 1, querying database..."` - when data comes from PostgreSQL
- `"Returning cached product: 1"` - when data comes from Redis

### 🛠️ **Docker Orchestration Learning**
- **Service Dependencies**: See how `depends_on` and `healthcheck` manage startup order.
- **Network Isolation**: Services communicate through Docker's internal network.
- **Volume Persistence**: Database and cache data persist between container restarts.

### 📈 **Understanding the Cache Statistics**
The statistics you see on the frontend are fetched directly from the Redis server's `INFO` command. They provide a real-time snapshot of the cache's performance. Here's what each metric means:

- **Cache Hits**: This is the number of times the application tried to get a product from the cache and **found it**. When this number goes up, it means Redis successfully served the data, and a slow database query was avoided. This is the goal of caching!

- **Cache Misses**: This is the number of times the application tried to get a product from the cache and **did not find it**. A cache miss is not an error; it's a normal part of the process. It simply means the data isn't in the cache yet, which triggers a query to the main database.

- **Hit Rate**: This is the most important metric for measuring cache effectiveness. It's the percentage of lookups that were successful hits. It's calculated with the formula:  
  `Hit Rate = (Cache Hits / (Cache Hits + Cache Misses)) * 100`  
  A high hit rate (e.g., > 90%) in a real-world application means your cache is working very efficiently.

- **Connected Clients**: This shows how many applications are currently connected to the Redis server. In our project, you will typically see **2 clients**:
    1. The **FastAPI backend**.
    2. **Redis Commander**, the GUI you use to view the cache.

- **Memory Used**: This shows the total amount of memory Redis is currently using to store your cached data. As you look up more products, you will see this number increase slightly.

- **Total Commands**: This is the total number of commands (like `GET`, `SET`, `PING`, etc.) that the Redis server has processed since it started.

## 📊 Understanding Cache Metrics

### Key Performance Indicators
- **Cache Hits**: Successful cache retrievals (fast responses)
- **Cache Misses**: Cache lookups that required database queries
- **Hit Rate**: `(Hits / (Hits + Misses)) × 100` - Higher is better!
- **Memory Usage**: Current Redis memory consumption
- **Connected Clients**: Active connections (typically 2: backend + Redis Commander)

### Performance Expectations
| Scenario | Response Time | Source |
|----------|---------------|---------|
| Cache Hit | 1-10ms | Redis |
| Cache Miss | 50-200ms | PostgreSQL |
| **Speed Improvement** | **10-100x faster** | Cache vs DB |

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

## 📄 License

MIT License - Feel free to use this project for learning and teaching purposes.