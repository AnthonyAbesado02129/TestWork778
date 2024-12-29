from sqlalchemy.orm import Session
from app.db.models import Transaction
from app.schemas.transaction import TransactionCreate
from heapq import heappush, heappop
from typing import List

def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    return db_transaction

def delete_all_transactions(db: Session):
    db.query(Transaction).delete()
    db.commit()

def get_statistics(db: Session):
    transactions = db.query(Transaction).all()
    
    # Calculate total and average
    total = len(transactions)
    average = sum(t.amount for t in transactions) / total if total > 0 else 0
    
    # Find top 3 transactions using heap
    heap = []
    for t in transactions:
        heappush(heap, (-t.amount, t.transaction_id))
    
    top_transactions = []
    for _ in range(min(3, total)):
        if heap:
            amount, tid = heappop(heap)
            top_transactions.append({"transaction_id": tid, "amount": -amount})
    
    return {
        "total_transactions": total,
        "average_transaction_amount": round(average, 2),
        "top_transactions": top_transactions
    }