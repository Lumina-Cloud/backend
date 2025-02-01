from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from src.core.database.model import BaseModel
from src.core.types.user_id import UserIDType

from .mixins import IdIntPkMixin


class User(BaseModel, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIDType]):
    pass
