from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, BaseModel
from typing import Literal
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


class LoggingConfig(BaseModel):
    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    log_format: str = LOG_DEFAULT_FORMAT

    @property
    def log_level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level.upper()]


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    user: str
    password: str
    host: str
    port: int
    name: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class AccessTokenConfig(BaseModel):
    lifetime: int = 3600


class Settings(BaseSettings):
    logging: LoggingConfig = LoggingConfig()
    database: DatabaseConfig
    access_token: AccessTokenConfig = AccessTokenConfig()

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


settings = Settings()
