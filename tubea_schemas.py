from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    _id: int = Field(default=None)
    user_name: str = Field(...)
    user_password: str = Field(...)



