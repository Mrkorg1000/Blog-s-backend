from pydantic import BaseModel
from typing import Optional


class SchemaAuthorBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class SchemaAuthorCreate(SchemaAuthorBase):
    pass


class SchemaAuthor(SchemaAuthorBase):
    id: int


class SchemaUpdateAuthor(SchemaAuthorBase):
    name: Optional[str]
    email: Optional[str]
