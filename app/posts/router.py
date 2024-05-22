from typing import List
from fastapi import APIRouter, Depends, Request
from sqlalchemy import select
from app.exceptions import ObjectAlreadyExistsException, ObjectDoesNotExistException
from app.posts.dao import PostDAO
from app.categories.dao import CategoryDAO
from app.posts.schemas import SchemaPost, SchemaPostCreate
from datetime import date


router = APIRouter(
    prefix="/posts",
    tags=["Посты"],
)


@router.post("", response_model=SchemaPost)
async def create_post(post: SchemaPostCreate):
    existing_category = await CategoryDAO.find_one_or_none(id=post.category_id)
    if not existing_category:
        raise ObjectDoesNotExistException

    new_post = await PostDAO.add(post)
    return new_post


@router.get("", response_model=List[SchemaPost])
async def get_authors_posts(author_id):
    return await PostDAO.find_all(author_id=int(author_id))
