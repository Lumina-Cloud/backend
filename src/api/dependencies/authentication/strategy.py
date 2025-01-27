from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from typing import TYPE_CHECKING, Annotated

from src.core.config import settings
from .access_token import get_accesstoken_db

if TYPE_CHECKING:
    from src.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
    accesstoken_db: Annotated[
        "AccessTokenDatabase[AccessToken]", Depends(get_accesstoken_db)
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=accesstoken_db, lifetime_seconds=settings.access_token.lifetime
    )
