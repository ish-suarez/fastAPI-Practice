from fastapi import APIRouter, HTTPException
from models import Customer
from database.customer import (
    get_all_customers,
    get_custer_by_id,
    create_customer,
    update_customer,
    delete_customer
)

router = APIRouter()


@router.get("/")
async def get_customers():
    customers = await get_all_customers()
    return customers

@router.get("/{customer_id}")
async def get_customer(customer_id: str):
    customer = await get_custer_by_id(customer_id)
    if customer:
        return customer
    else:
        raise HTTPException(status_code=404, detail="Customer not found")

@router.post("/")
async def post_customer(customer: Customer):
    created_customer = await create_customer(customer.model_dump())
    return created_customer

@router.put("/{customer_id}")
async def put_customer(customer_id: str, customer: Customer):
    updated_customer = await update_customer(customer_id, customer.model_dump(exclude_unset=True))
    if not updated_customer: 
        raise HTTPException(status_code=404, detail="Customer not found")
    return { "message": "Customer updated successfully" }

@router.delete("/{customer_id}")
async def remove_customer(id: str):
    deleted_customer = await delete_customer(id)
    if not deleted_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return { "message": "Customer deleted successfully" }