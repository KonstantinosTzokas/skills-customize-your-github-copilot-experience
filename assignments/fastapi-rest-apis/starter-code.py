"""
FastAPI REST API Starter Code

This starter template provides a basic structure for building a REST API.
Complete the implementation by adding the necessary endpoints and logic.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI(title="REST API Assignment", version="1.0.0")

# Pydantic model for request/response validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


# In-memory data store (simulating a database)
items_db = [
    {"id": 1, "name": "Laptop", "description": "High-performance laptop", "price": 999.99},
    {"id": 2, "name": "Keyboard", "description": "Mechanical keyboard", "price": 149.99},
]


# TODO: Implement GET endpoint to retrieve all items
# Route: GET /items
# Should return a list of all items


# TODO: Implement GET endpoint to retrieve a specific item by ID
# Route: GET /items/{item_id}
# Should return a single item or raise 404 if not found


# TODO: Implement POST endpoint to create a new item
# Route: POST /items
# Should accept an Item object and add it to the database
# Should return the created item with an assigned ID


# TODO: Implement PUT endpoint to update an existing item
# Route: PUT /items/{item_id}
# Should accept an Item object and update the item in the database
# Should raise 404 if item not found


# TODO: Implement DELETE endpoint to remove an item
# Route: DELETE /items/{item_id}
# Should remove the item from the database
# Should raise 404 if item not found


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
