import fastapi
from pydantic import BaseModel

class Vote(BaseModel):
    message: str


app = fastapi.FastAPI()

item = [
    "말레이시아 코타키나발루",
    "인도네시아 롬복",
    "필리핀 세부",
    "태국 푸켓",
    "캄보디아 시아누크빌"
]
votes = [0] * len(item)

@app.get('/')
def index():
    return{
       "link":{
        "current":"/items"
       },
       "data":item
    }

@app.get('/items')
def items():
    data = []
    for num, name in enumerate(item):
        data.append({
            "type":"LOCATION",
            "link":f"/item/{num+1}",
            "id":num+1,
            "data":{
                "name":name
            }
        })
    return {
        "link":{
            "current":"/items"
        },
        "data":data
    }

@app.get('/item/{_id}')
def get_item(_id: int):
    if _id <= 0 or _id > len(item):
        raise fastapi.HTTPException(
            status_code=404,
            detail="Item not found",
            headers={
                "X-Error": f"{_id} does not exist."
            }
        )
    return {
        "type":"LOCATION",
        "id":_id,
        "data":{
            "name": item[_id-1]
        }
    }

@app.post('/item/{_id}')
def vote_item(_id:int, vote:Vote):
    if _id <= 0 or _id > len(votes) or _id > len(item):
        raise fastapi.HTTPException(
            status_code=404,
            detail="Item not found",
            headers={
                "X-Error": f"{_id} does not exist."
            }
        )
    votes[_id-1] = votes[_id-1] + 1
    return {
        "type":"LOCATION",
        "id":_id,
        "data":{
            "name": item[_id-1],
            "vote": votes[_id-1]
        }
    }
