from fastapi import APIRouter

from src.api.dependencies.authentication.fastapi_users_routers import (
    fastapi_users_routers,
)
from src.api.dependencies.authentication.backend import authentication_backend

router = APIRouter(prefix="/auth", tags=["Authentication"])

router.include_router(
    router=fastapi_users_routers.get_auth_router(authentication_backend),
)
