# Handles all the operations - CRUD - Create, Read, Update, Delete

from src.user import controller
from src.utils.db import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status,Request
from src.user.dtos import UserRegisterSchema, UserRegisterResponseSchema, UserLoginSchema

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model = UserRegisterResponseSchema, status_code = status.HTTP_201_CREATED)
def register(body: UserRegisterSchema, db: Session = Depends(get_db)):
    return controller.register_user(body, db)


@user_routes.post("/login", status_code = status.HTTP_200_OK)
def login(body:UserLoginSchema, db:Session = Depends(get_db)):
    return controller.login_user(body, db)


@user_routes.get("/is_auth", response_model = UserRegisterResponseSchema, status_code = status.HTTP_200_OK)
def is_auth(request:Request, db:Session = Depends(get_db)):
    return controller.is_authenticated(request, db)