## How to validate data - DTOS - Data Transfer Objects
## pydantic - data validation, data parsing, data serialization, data deserialization
from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    title: str
    price: float = 0
    count: int = 0