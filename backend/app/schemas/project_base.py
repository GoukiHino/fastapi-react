from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True
