from pydantic import BaseModel
from datetime import time,date

class PaymentBase(BaseModel):
    enrollment_id: int
    payment_date: date
    payment_month: date

class PaymentCreate(PaymentBase):
    pass  # Used when creating a new payment

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True

