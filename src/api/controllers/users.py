from fastapi import APIRouter

from src.api.dependencies.authentication import fastapi_users_routers
from src.api.schemas.user import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

router.include_router(
    router=fastapi_users_routers.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
