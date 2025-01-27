from fastapi import APIRouter

from .auth import router as auth_router

api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)

__all__: tuple = ("api_router",)
