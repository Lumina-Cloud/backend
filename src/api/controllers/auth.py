from fastapi import APIRouter

from src.api.dependencies.authentication import fastapi_users_routers
from src.api.dependencies.authentication import authentication_backend
from src.api.schemas.user import UserRead, UserCreate

router = APIRouter(prefix="/auth", tags=["Authentication"])

router.include_router(
    router=fastapi_users_routers.get_auth_router(
        authentication_backend,
    ),
)

router.include_router(
    router=fastapi_users_routers.get_register_router(
        UserRead,
        UserCreate,
    )
)
