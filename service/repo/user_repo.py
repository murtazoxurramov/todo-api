from sqlalchemy import insert, select
from models.db.user import User
from service.repo.base_repo import BaseSQLAlchemyRepo


class UserRepo(BaseSQLAlchemyRepo):
    model = User

    async def add_user(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
    ) -> None:
        sql = insert(self.model).values(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        await self._session.execute(sql)
        await self._session.commit()

    async def get_user(self, email: str) -> model or None:
        sql = select(self.model).filter(self.model.email == email)
        request = await self._session.execute(sql)
        return request.scalar()
