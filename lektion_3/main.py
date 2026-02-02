from fastapi import FastAPI,status
import requests
from typing import Union
from schema.user import UserSchema,UserSchemaOut
from schema.fox import FoxSchema

userList: list[UserSchema] = [
    UserSchema(username='a', password='b'),
    UserSchema(username='d', password='g')
]

app = FastAPI(title="My First API APP")

@app.get("/")
def root():
    return {'Hello': 'World'}

@app.get("/items/{item_id}") # localhost:8000/items/248?color=black
def get_item(item_id: int, color: Union[str, None] = None):
    return {"item_id": item_id, "color": color}

@app.get("/users", response_model=list[UserSchemaOut])
def get_users() -> list[UserSchemaOut]:
    return userList

@app.post(
        '/users',
        response_model=UserSchema,
        status_code=status.HTTP_201_CREATED)
def post_user(user: UserSchema) -> UserSchema:
    userList.append(user)
    return user

@app.get('/fox', response_model=FoxSchema)
def get_fox():
    response = requests.get('https://randomfox.ca/floof/')
    result_json = response.json()
    print(f"DEBUGGING {result_json}")
    fox = FoxSchema(**result_json) # Convert JSON to python object
    fox = fox.image()
    return fox