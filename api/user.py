from fastapi import APIRouter, FastAPI, Depends, HTTPException
from fastapi import APIRouter, HTTPException
from application.user.dto import UserSchema
from application.user.queries.get_user_query import GetUserHandler, GetUserQuery
from infraestructure.unit_of_work import SqlAlchemyUnitOfWork
from utils.exceptions import UserNotFoundException




router = APIRouter()

@router.get("/users/{user_id}", response_model=UserSchema)
def get_user(user_id: str):
     with SqlAlchemyUnitOfWork() as uow:
         handler = GetUserHandler(uow)
         try:
             user = handler.get_user_handler(GetUserQuery(user_id))
             return user
         except UserNotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
         








