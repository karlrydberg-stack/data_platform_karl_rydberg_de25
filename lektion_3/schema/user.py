from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str

class UserSchemaOut(BaseModel):
    username: str