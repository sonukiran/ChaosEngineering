# app/main.py
from fastapi import FastAPI, HTTPException
from typing import List
from app.database import read_items, write_items
from app.models import Item

app = FastAPI()

# GET endpoint to retrieve all items
@app.get("/items", response_model=List[Item])
async def get_items():
    return read_items()

# GET endpoint to retrieve a single item by its ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    items = read_items()
    # Search for the item with the specified ID
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# GET endpoint to retrieve a single item by its ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    items = read_items()
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# POST endpoint to create a new item
# POST endpoint to create a new item with item_id in the path
@app.post("/items/{item_id}", response_model=Item)
async def create_item(item_id: int, item: Item):
    items = read_items()
    # Ensure the item ID matches the path
    if item.id != item_id:
        raise HTTPException(status_code=400, detail="Item ID in the body does not match the path ID")
    # Check if an item with the same ID already exists
    if any(existing_item["id"] == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    # Add the new item and save it to the JSON file
    items.append(item.dict())
    write_items(items)
    return item


# PUT endpoint to update an existing item by ID
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    items = read_items()
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = updated_item.dict()
            write_items(items)
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE endpoint to delete an item by ID
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    items = read_items()
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items = [item for item in items if item["id"] != item_id]
    write_items(items)
    return item
