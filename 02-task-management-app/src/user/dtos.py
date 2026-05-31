# DTOs - Data Transfer Objects - This is used to transfer data between layers
# This is used to define the shape of the data that is sent between the client and the server

from pydantic import BaseModel

class UserRegisterSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str

class UserRegisterResponseSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str


class UserLoginSchema(BaseModel):
    username: str
    password: str

class UserLoginResponseSchema(BaseModel):
    token: str