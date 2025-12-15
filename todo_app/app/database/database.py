from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017/fastapi_todo"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.fastapi_todo

# Collections
items_collection = database.get_collection("items")
customers_collection = database.get_collection("customers")