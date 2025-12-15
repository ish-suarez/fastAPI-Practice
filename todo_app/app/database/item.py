from database.database import items_collection
from bson import ObjectId

def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item.get("name", ""),  # Default to an empty string if the field is missing
        "description": item.get("description", ""),
        "price": item.get("price", 0.0),  # Default to 0.0 for missing price
        "in_stock": bool(item.get("in_stock", False)),  # Default to False for missing in_stock
    }

async def get_items():
    items = []
    async for item in items_collection.find():
        items.append(item_helper(item))
    return items

async def add_item(item_data: dict) -> dict:
    item = await items_collection.insert_one(item_data)
    new_item = await items_collection.find_one({"_id": item.inserted_id})
    return item_helper(new_item)

async def get_item(id: str) -> dict:
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item_helper(item)
    else: 
        return dict()
    
async def update_selected_item(id: str, data: dict):
    if len(data) < 1:
        return False
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        update_item = await items_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if update_item:
            return True
    return False

async def delete_item(id: str):
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        await items_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False