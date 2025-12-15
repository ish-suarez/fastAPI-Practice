from database.database import customers_collection
from bson import ObjectId

def customer_helper(customer) -> dict:
    return {
        "id": str(customer["_id"]),
        "name": customer["name"],
        "email": customer["email"],
    }
    
async def get_all_customers():
    customers = []
    async for customer in customers_collection.find():
        customers.append(customer_helper(customer))
    return customers

async def get_custer_by_id(id: str) -> dict:
    customer = await customers_collection.find_one({"_id": ObjectId(id)})
    if customer:
        return customer_helper(customer)
    return dict()

async def create_customer(customer_data: dict) -> dict:
    customer = await customers_collection.insert_one(customer_data)
    new_customer = await customers_collection.find_one({"_id": customer.inserted_id})
    return customer_helper(new_customer)
    
async def update_customer(id: str, data: dict):
    if len(data) < 1:
        return False
    customer = await customers_collection.find_one({"_id": ObjectId(id)})
    if customer: 
        updated_customer = await customers_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_customer:
            return True
    return False

async def delete_customer(id: str):
    customer = await customers_collection.find_one({"_id": ObjectId(id)})
    if customer:
        await customers_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
