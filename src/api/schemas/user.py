from fastapi_users import schemas

from src.core.types.user_id import UserIDType


class UserRead(schemas.BaseUser[UserIDType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
