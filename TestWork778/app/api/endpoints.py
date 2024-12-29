from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.transaction import TransactionCreate, TransactionResponse, Statistics
from app.services.transaction_service import create_transaction, delete_all_transactions, get_statistics
from app.core.security import get_api_key
import uuid

router = APIRouter(dependencies=[Depends(get_api_key)])

@router.post("/transactions", response_model=TransactionResponse)
def add_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    try:
        create_transaction(db, transaction)
        return {
            "message": "Transaction received",
            "task_id": str(uuid.uuid4())
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/transactions")
def remove_transactions(db: Session = Depends(get_db)):
    delete_all_transactions(db)
    return {"message": "All transactions deleted"}

@router.get("/statistics", response_model=Statistics)
def read_statistics(db: Session = Depends(get_db)):
    return get_statistics(db)