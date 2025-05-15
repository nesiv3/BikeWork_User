


from infraestructure.models.database import SessionLocal
from infraestructure.repositories.user_repository import UserRepository


class IUnitOfWork:
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def commit(self): ...
    @property
    def user(self): ...

class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session = SessionLocal()
        self._user = UserRepository(self.session)
       
       

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.commit()
        self.session.close()

    def commit(self):
        self.session.commit()

    @property
    def user(self):
        return self._user
    







