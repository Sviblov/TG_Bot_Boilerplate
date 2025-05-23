from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.repo.users import UserRepo
from infrastructure.database.repo.interface import InterfaceRepo
from infrastructure.database.repo.log_message import logMessageRepo
from infrastructure.database.repo.payment import PaymentRepo

from infrastructure.database.setup import create_engine


@dataclass
class RequestsRepo:
    """
    Repository for handling database operations. This class holds all the repositories for the database models.

    You can add more repositories as properties to this class, so they will be easily accessible.
    """

    session: AsyncSession

    @property
    def users(self) -> UserRepo:
        """
        The User repository sessions are required to manage user operations.
        """
        return UserRepo(self.session)
    
    @property
    def interface(self) -> InterfaceRepo:
        """
        The User repository sessions are required to manage user operations.
        """
        return InterfaceRepo(self.session)
    

    @property
    def log_message(self) -> logMessageRepo:

        return logMessageRepo(self.session)

    @property
    def payment(self) -> PaymentRepo:

        return PaymentRepo(self.session)



if __name__ == "__main__":
    from infrastructure.database.setup import create_session_pool
    from infrastructure.config import Config

    async def example_usage(config: Config):
        """
        
        """
        engine = create_engine(config.db)
        session_pool = create_session_pool(engine)

        async with session_pool() as session:
            repo = RequestsRepo(session)

            # Replace user details with the actual values
            user = await repo.users.get_or_create_user(
                user_id=12356,
                full_name="Mr Smith",
                language="ru",
                username="smith",
            )
