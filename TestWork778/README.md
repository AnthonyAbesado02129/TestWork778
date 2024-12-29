# Financial Transaction Analysis Microservice

A REST API microservice for processing and analyzing financial transactions.

## Features

- Transaction management via REST API
- Statistical analysis of transactions
- Asynchronous processing with Celery
- API key authentication
- PostgreSQL database storage
- Docker containerization

## Running Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TestWork778.git
cd TestWork778
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/transactions_db"
export REDIS_URL="redis://localhost:6379/0"
export API_KEY="your_secret_api_key"
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

## Running with Docker Compose

1. Build and start the containers:
```bash
docker-compose up --build
```

2. The API will be available at http://localhost:8000

## API Documentation

Once the application is running, visit http://localhost:8000/docs for the Swagger documentation.

## Running Tests

```bash
pytest
```

## API Endpoints

- POST /transactions - Upload a new transaction
- DELETE /transactions - Delete all transactions
- GET /statistics - Get transaction statistics

## Security

All endpoints require an API key passed in the Authorization header:
```
Authorization: ApiKey your_secret_api_key
```