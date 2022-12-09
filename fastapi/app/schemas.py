from email import message
from typing import List, Union

from pydantic import BaseModel

class VoteMessageBase(BaseModel):
    message: str

class VoteMessage(VoteMessageBase):
    id: int
    item_id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    name: str
    vote: int

class Item(ItemBase):
    id: int
    messages: List[VoteMessage] = []

    class Config:
        orm_mode = True

class ItemCreate(ItemBase):
    pass

class VoteMessageCreate(VoteMessageBase):
    pass

class ItemResponse(BaseModel):
    type: str
    link: str
    id: int
    data: Item

class ItemsResponse(BaseModel):
    link: dict
    data: List[ItemResponse]
