from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
app = FastAPI()
# Fake Database (Dictionary)
items_db: Dict[int, dict] = {}
# Pydantic Model
class Item(BaseModel):
name: str
price: float
description: str = None
# Home Route
@app.get("/")
def read_root():
return {"message": "Welcome to FastAPI CRUD App"}
# Create an Item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
if item_id in items_db:
raise HTTPException(status_code=400, detail="Item already
exists")
items_db[item_id] = item.dict()
return {"message": "Item created", "item": items_db[item_id]}
# Read an Item
@app.get("/items/{item_id}")
def read_item(item_id: int):
if item_id not in items_db:
raise HTTPException(status_code=404, detail="Item not
found")
return items_db[item_id]
# Update an Item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
if item_id not in items_db:
raise HTTPException(status_code=404, detail="Item not
found")
items_db[item_id] = item.dict()
return {"message": "Item updated", "item": items_db[item_id]}
# Delete an Item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
if item_id not in items_db:
raise HTTPException(status_code=404, detail="Item not
found")
del items_db[item_id]
return {"message": "Item deleted"}
# Run the app
if __name__ == "__main__":
import uvicorn
uvicorn.run(app, host="127.0.0.1", port=8000)
