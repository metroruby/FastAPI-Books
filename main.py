from fastapi import FastAPI, Path, Query

app = FastAPI()

fake_items_db = [
    {
      "item_id": "1",
      "name": "Game of thrones"
    },
    {
      "item_id": "2",
      "name": "Clash of kings"
    }
]


@app.get("/books/")
async def read_item():
    return fake_items_db

@app.get("/books/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: str = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results