from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

__all__: tuple = ("api_router",)
