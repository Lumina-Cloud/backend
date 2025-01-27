from fastapi import APIRouter

from .auth import router as auth_router

api_router = APIRouter(prefix="/api")

__all__: tuple = ("api_router", "auth_router")
