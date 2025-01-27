from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from typing import TYPE_CHECKING, Annotated

from src.models import AccessToken
from src.core.database.db_helper import db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_accesstoken_db(
    session: Annotated["AsyncSession", Depends(db_helper.session_getter)],
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
