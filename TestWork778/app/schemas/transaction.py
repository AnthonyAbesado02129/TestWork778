from pydantic import BaseModel
from datetime import datetime
from typing import List

class TransactionCreate(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    currency: str
    timestamp: datetime

class TransactionResponse(BaseModel):
    message: str
    task_id: str

class TopTransaction(BaseModel):
    transaction_id: str
    amount: float

class Statistics(BaseModel):
    total_transactions: int
    average_transaction_amount: float
    top_transactions: List[TopTransaction]