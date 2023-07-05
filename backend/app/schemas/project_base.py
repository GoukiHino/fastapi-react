from pydantic import BaseModel


class ProjectBase(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True
