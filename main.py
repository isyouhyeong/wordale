# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

answer='APPLE'

@app.get('/answer')
def get_answer():
    return answer

app.mount("/", StaticFiles(directory="static",html=True), name="static")




















# class Item(BaseModel):
#     id:int
#     content:str

# items = ['맥북','애플워치','아이폰','에어팟']


# @app.get('/items/{id}')
# def read_id_item(id):
#     return items[int(id)]


# @app.get('/items')
# def read_item(skip: int = 0, limit: int = 0):
#     return items[skip: skip+limit]


# @app.post("/items")
# def post_item(item:Item):
#     items.append(item.content)
#     return '성공했습니다!'

# # 이 파일을 실행하려면 다음 명령어를 사용합니다.
# # uvicorn main:app --reload

