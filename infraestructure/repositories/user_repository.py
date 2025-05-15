from sqlalchemy.orm import Session, joinedload,lazyload

from infraestructure.models.database import UserORM


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: str):
         return (
             self.db.query(UserORM)
             .filter(UserORM.id == user_id)
             .first()
         )

    def get_user_with_profile_and_roles(self, user_id: str):
        return (
            self.db.query(UserORM)
            .filter(UserORM.id == user_id)
            .first()
        )