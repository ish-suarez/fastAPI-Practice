from fastapi import APIRouter, HTTPException
from models import Item
from database.item import (
    get_items,
    get_item,
    add_item,       
    update_selected_item,
    delete_item
)

router = APIRouter()

@router.get("/")
async def retrieve_items():
    items = await get_items()
    return items

@router.get("/{id}")
async def get_item_by_id(id: str):
    item = await get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/")
async def post_new_item(item: Item):
    new_item = await add_item(item.model_dump())
    return new_item

@router.put("/{id}")
async def update_item (id: str, item: Item):
    updated_item = await update_selected_item(id, item.model_dump(exclude_unset=True))
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated successfully"}

@router.delete("/{id}")
async def delete_item_by_id(id: str):
    deleted = await delete_item(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}