# DTOs - Data Transfer Objects - This is used to transfer data between layers
# This is used to define the shape of the data that is sent between the client and the server

from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool=False


class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id: int | None = 0