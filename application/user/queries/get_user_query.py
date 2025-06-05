
from application.user.dto import UserSchema
from infraestructure.unit_of_work import IUnitOfWork
from utils.exceptions import UserNotFoundException


class GetUserQuery:
    def __init__(self, user_id: str):
        self.user_id = user_id

class GetUserHandler:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def get_user_handler(self, query: GetUserQuery):
        user = self.uow.user.get_user(query.user_id)
        if not user:
            raise UserNotFoundException(query.user_id)
        user_dto = UserSchema.from_orm(user)
        return user_dto
    

    def get_user_profile_role_handler(self, query: GetUserQuery):
        user = self.uow.user.get_user_with_profile_and_roles(query.user_id)
        if not user:
            raise UserNotFoundException(query.user_id)
        user_dto = UserSchema.from_orm(user)
        return user_dto