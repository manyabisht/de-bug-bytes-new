from pydantic import BaseModel
from typing import Optional

class TravelPackage(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float
    duration: int  # Duration in days

class Customer(BaseModel):
    id: Optional[int]
    name: str
    email: str
    agent_id: str
