from email import message
from sqlalchemy.orm import Session

from . import models, schemas

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(
        models.Item.id == item_id
    ).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_vote_messages_by_item(db: Session, item_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.VoteMessage).filter(
        models.VoteMessage.item_id == item_id
    ).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_vote_message(db: Session, vote: schemas.VoteMessage, item_id: int):
    db_vote = models.VoteMessage(
        message=vote.message,
        item_id=item_id
    )
    db.add(db_vote)
    item = get_item(db, item_id)
    item.vote = item.vote + 1
    db.add(item)
    db.commit()
    db.refresh(db_vote)
    return db_vote