from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database.model import BaseModel
from src.core.types.user_id import UserIDType


class AccessToken(BaseModel, SQLAlchemyBaseAccessTokenTable[UserIDType]):
    user_id: Mapped[UserIDType] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )
