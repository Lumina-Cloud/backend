from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.model import BaseModel
from src.core.database.db_helper import db_helper
from src.core.types.user_id import UserIDType
from .mixins import IdIntPkMixin


class User(BaseModel, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIDType]):
    pass


async def get_user_db(session: AsyncSession = Depends(db_helper.session_getter)):
    yield SQLAlchemyUserDatabase(session, User)
