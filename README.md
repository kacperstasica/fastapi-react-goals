# Goals Tracking Application

Small full-stack goals tracking application with FastAPI backend, React frontend, and MongoDB database.

## Architecture

- **Backend**: Python FastAPI
- **Frontend**: React 18
- **Database**: MongoDB 7.0
- **Orchestration**: Docker Compose

## Quick Start

### 1. Clone and Setup

```bash
cd fastapi-react-goals
cp .env.example .env
# Edit .env with your credentials
```

### 2. Start with Docker Compose

```bash
# Start all services (frontend + backend + mongodb)
docker-compose up -d --build

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f backend

# Stop services
docker-compose down

# Stop and remove volumes (deletes data!)
docker-compose down -v
```

### 3. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:80
- **API Docs**: http://localhost:80/docs

## Security Features

✅ MongoDB authentication enabled  
✅ Database not exposed to host (internal network only)  
✅ Environment variable configuration  
✅ Isolated Docker network  
✅ Persistent data with named volumes

## Architecture

```
User Browser (http://localhost:3000)
    ↓
Frontend Container (React)
    ↓ (http://localhost:80)
Backend Container (FastAPI)
    ↓ (mongodb://mongodb:27017)
MongoDB Container
    ↓
Named Volume (mongodb_data)
```
