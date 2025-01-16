from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

@app.get("/")
def root():
    return {"hello": "world"}

items = []

@app.post("/item")
def collect_items(item: Item):
    items.append(item)
    return items

@app.get("/item/{item id}")
def get_item(item_id: int):
    if item_id < len(items):
        item = items[item_id]
        return item
    else:
        raise HTTPException(status_code=404,detail="Item not found")