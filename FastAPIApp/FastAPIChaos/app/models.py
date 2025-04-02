# app/models.py
from pydantic import BaseModel


# Define the Item schema
class Item(BaseModel):
    id: int
    name: str
    description: str = None
