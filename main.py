from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from flask import make_response, abort

class BookIn(BaseModel):
    tname: str = None
    author: str = None

app = FastAPI()

BOOKSTORE = {
    "Measure What Matters": {
        "tname": "Measure What Matters",
        "author": "John Doerr",
    },
    "Misbehaving": {
        "tname": "Misbehaving",
        "author": "Richard H. Thaler",
    },
    "Pre-Suasion": {
        "tname": "Pre-Suasion",
        "author": "Robert Caildini",
    },
}

@app.get("/books/")
async def read_all():
    return [BOOKSTORE[key] for key in sorted(BOOKSTORE.keys())]

@app.get("/books/{tname}")
async def read_one(tname):
    if tname in BOOKSTORE:
        titelbook = BOOKSTORE.get(tname)
    else:
        abort(
            404, "Book with last name {tname} not found".format(author=author)
        )
    return titelbook

def fake_save_book(book_in: BookIn):
    book_in_db = BookIn(**book_in.dict())
    print("Book saved!")
    return book_in_db

@app.post("/books/", response_model=BookIn)
async def create_book(*, book_in: BookIn):
    book_saved = fake_save_book(book_in)
    return book_saved
