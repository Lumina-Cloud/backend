from fastapi_users import FastAPIUsers

from src.models import User
from src.core.types.user_id import UserIDType
from .user_manager import get_user_manager
from .backend import authentication_backend

fastapi_users_routers = FastAPIUsers[User, UserIDType](
    get_user_manager,
    [authentication_backend],
)
