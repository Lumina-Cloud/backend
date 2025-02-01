from fastapi import APIRouter

from src.api.dependencies.authentication import authentication_backend, fastapi_users_routers
from src.api.schemas.user import UserCreate, UserRead

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
