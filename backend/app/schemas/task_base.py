from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True
