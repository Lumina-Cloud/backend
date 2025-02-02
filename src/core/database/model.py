from sqlalchemy.orm import DeclarativeBase, declared_attr
from src.utils.db_naming import generate_tablename

class BaseModel(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return generate_tablename(cls)
