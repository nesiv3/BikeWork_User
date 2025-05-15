class AppException(Exception):
    pass

class NotFoundException(AppException):
    def __init__(self, name: str):
        super().__init__(f"{name} not found")

class UserNotFoundException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.message = f"User with id {user_id} not found"
        super().__init__(self.message)

