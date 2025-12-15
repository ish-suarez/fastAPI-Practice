from bson import ObjectId
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}  # Custom encoder for ObjectId
        
class Customer(BaseModel):
    name: str
    email: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}  # Custom encoder for ObjectId