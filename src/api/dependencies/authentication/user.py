from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.core.database.db_helper import db_helper
from src.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated["AsyncSession", Depends(db_helper.session_getter)],
):
    yield SQLAlchemyUserDatabase(session, User)
