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

# 내가 추가한 함수. 맞을거라 생각함.
@app.get('/item/{_id}', response_model=schemas.ItemResponse)
def get_item(_id: int, skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    if _id <= 0 or _id > len(items):
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={
                "X-Error": f"{_id} does not exist."
            }
        )
    item = items[_id-1]
    return {
        "type": "LOCATION",
        "link": f"/item/{item.id}",
        "id": item.id,
        "data": item
    }

# 내가 추가한 함수. 원래는 @app.post("/item/{_id}", ...)로 만들어야하는데 vote내부의 item_id랑 _id가 중복된 값인것 같아서 없애버림. VoteResponse도 내가 만든거
@app.post('/item',response_model=schemas.VoteResponse)
def vote_item(vote: schemas.VoteMessage, db: Session=Depends(get_db)):
    vote_message = crud.create_vote_message(db, vote=vote, item_id=vote.item_id)
    return {
        "type": "MESSAGE",
        "id": vote_message.id,
        "data": vote_message
    }