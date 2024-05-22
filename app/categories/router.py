from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from app.categories.dao import CategoryDAO
from app.categories.schemas import SchemaCategory, SchemaCategoryCreate


from app.exceptions import ObjectAlreadyExistsException


router = APIRouter(
    prefix="/categories",
    tags=["Категории"],
)


@router.post("", response_model=SchemaCategory)
async def create_category(category: SchemaCategoryCreate):
    existing_category = await CategoryDAO.find_one_or_none(name=category.name)
    if existing_category:
        raise ObjectAlreadyExistsException

    new_category = await CategoryDAO.add(category)
    return new_category


@router.get("", response_model=List[SchemaCategory])
async def get_categories():
    return await CategoryDAO.get_all_objects()
