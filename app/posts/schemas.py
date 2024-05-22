from pydantic import BaseModel
import datetime


class SchemaPostBase(BaseModel):
    title: str
    content: str
    author_id: int
    category_id: int

    class Config:
        orm_mode = True


class SchemaPostCreate(SchemaPostBase):
    pass


class SchemaPost(SchemaPostBase):
    id: int
    created_at: datetime.datetime
