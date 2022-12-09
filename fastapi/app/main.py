from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 의존성 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/items', response_model=schemas.ItemsResponse)
def items(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    data = []
    for item in items:
        data.append({
            "type": "LOCATION",
            "link": f"/item/{item.id}",
            "id": item.id,
            "data": item
        })
    return {
        "link":{
            "current": "/items"
        },
        "data": data
    }

@app.post('/items', response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session=Depends(get_db)):
    db_item = crud.create_item(db, item)
    return {
        "type": "LOCATION",
        "link": f"/item/{db_item.id}",
        "id": db_item.id,
        "data": db_item
    }

# 내가 추가한 함수
@app.get('/item/{_id}', response_model=schemas.ItemResponse)
def get_item(_id: int, db: Session=Depends(get_db)):
    item = crud.get_item(db, _id)
    return {
        "type": "LOCATION",
        "link": f"/item/{item.id}",
        "id": item.id,
        "data": item
    }

# 내가 추가한 함수.
@app.post('/item/{_id}', response_model=schemas.ItemResponse)
def vote_item(_id: int, item: schemas.VoteMessageCreate, db: Session=Depends(get_db)):
    crud.create_vote_message(db, item, _id)
    item = crud.get_item(db, _id)
    return {
        "type": "LOCATION",
        "link": f"/item/{item.id}",
        "id": item.id,
        "data": item
    }