from pydantic import BaseModel


class UserBase(BaseModel):
    display_name: str
    email: str

    class Config:
        orm_mode = True
