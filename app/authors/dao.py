from sqlalchemy import select
from app.dao.base import BaseDAO
from app.authors.models import Author
from app.database import async_session_maker
from app.exceptions import ObjectDoesNotExistException


class AuthorDAO(BaseDAO):
    model = Author

    @classmethod
    async def update_author(cls, author_id, author_update_scheme):
        async with async_session_maker() as session:
            author_to_update = await session.get(cls.model, author_id)
            if not author_to_update:
                raise ObjectDoesNotExistException

            update_data = author_update_scheme.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(author_to_update, key, value)
            
            await session.commit()
            await session.refresh(author_to_update)
            return author_to_update
