from typing import List
from fastapi import APIRouter
from app.authors.dao import AuthorDAO
from app.authors.schemas import SchemaAuthorCreate, SchemaAuthor, SchemaUpdateAuthor
from app.exceptions import ObjectAlreadyExistsException, ObjectDoesNotExistException


router = APIRouter(
    prefix="/authors",
    tags=["Авторы"],
)


@router.post("", response_model=SchemaAuthor)
async def create_author(author: SchemaAuthorCreate):
    existing_author = await AuthorDAO.find_one_or_none(name=author.name)
    if existing_author:
        raise ObjectAlreadyExistsException

    new_author = await AuthorDAO.add(author)
    return new_author


@router.delete("/{name}")
async def delete_author(name):
    author_to_delete = await AuthorDAO.find_one_or_none(name=name)
    if not author_to_delete:
        raise ObjectDoesNotExistException

    await AuthorDAO.delete(author_to_delete)


@router.get("", response_model=List[SchemaAuthor])
async def get_authors():
    return await AuthorDAO.get_all_objects()


@router.patch("/{id}", response_model=SchemaAuthor)
async def update_author(author_id, author_update_scheme: SchemaUpdateAuthor):
    return await AuthorDAO.update_author(int(author_id), author_update_scheme)
