from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database.model import BaseModel
from src.core.database.db_helper import db_helper
from .mixins import IdIntPkMixin


class UserModel(BaseModel, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass


async def get_user_db(session: AsyncSession = Depends(db_helper.session_getter)):
    yield SQLAlchemyUserDatabase(session, UserModel)
