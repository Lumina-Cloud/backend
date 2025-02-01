from fastapi_users import FastAPIUsers

from src.core.types.user_id import UserIDType
from src.models import User

from .backend import authentication_backend
from .user_manager import get_user_manager

fastapi_users_routers = FastAPIUsers[User, UserIDType](
    get_user_manager,
    [authentication_backend],
)
