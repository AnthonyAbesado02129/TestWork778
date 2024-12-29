from fastapi import FastAPI
from app.api.endpoints import router
from app.db.database import Base, engine

app = FastAPI(title="Financial Transaction Analysis Service")

Base.metadata.create_all(bind=engine)

app.include_router(router)