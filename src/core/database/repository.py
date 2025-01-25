from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import TypeVar, Generic, Type
from src.core.database.model import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepository(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, session: AsyncSession):
        if not self.model:
            raise NotImplementedError(
                message=("Can not initiate the class without model attribute")
            )

        self.session = session

    async def create(self, **attributes) -> ModelType:
        """
        Creates the model instance.

        :param attributes: The attributes to create the model with.
        :return: The created model instance.
        """
        if attributes is None:
            attributes = {}
        model = self.model(**attributes)
        self.session.add(model)
        self.session.commit()
        return model

    async def get(self, key: str) -> ModelType | None:
        """
        Return only one result by id

        :param key: The id of the instance
        :return: The instance
        """
        result = await self.session.get(self.model, key)

        return result

    async def get_by(self, **filter_by) -> ModelType | None:
        """
        Return only one result by filters

        :param filter_by: The filters
        :return: The instance
        """
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)

        return result.scalar_one_or_none()

    async def get_all(self, **filter_by) -> list[ModelType] | None:
        """
        Return all results by filters

        :param filter_by: The filters
        :return: The instances
        """
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)

        return result.scalars().all()
