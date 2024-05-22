from pydantic import BaseModel


class SchemaCategoryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SchemaCategoryCreate(SchemaCategoryBase):
    pass


class SchemaCategory(SchemaCategoryBase):
    id: int
