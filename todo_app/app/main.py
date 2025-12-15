from fastapi import FastAPI
from routes.items import router as ItemRouter
from routes.customers import router as CustomerRouter

app = FastAPI()

app.include_router(ItemRouter, prefix="/items", tags=["Items"])
app.include_router(CustomerRouter, prefix="/customers", tags=["Customers"])

@app.get('/')
def root():
    return {"message": "Welcome to the FastAPI NoSQL application"}  