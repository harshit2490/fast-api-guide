# Controller handles the business logic - Perform operations on the user data
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#about-jwt
# 1. pip install pyjwt - To generate and verify the JWT tokens in Python.
# 2. pip install "pwdlib[argon2]" - This is used to hash the password.

import jwt
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.utils.settings import settings
from datetime import datetime, timedelta
from jwt.exceptions import InvalidTokenError
from fastapi import Request, HTTPException, status
from src.user.dtos import UserRegisterSchema, UserLoginSchema

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(password, hash_password):
    return password_hash.verify(password, hash_password)


def register_user(body: UserRegisterSchema, db: Session):
    ## 1. Username validation
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Username already exists...")
    
    ## 2. Email validation
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Email address already exists...")

    ## 3. Hashing the password
    hash_password = get_password_hash(body.password)

    ## 4. Create user object
    new_user = UserModel(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(body: UserLoginSchema, db: Session):
    ## 1. Username validation
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "You entered wrong username...")

    ## 2. Password validation
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "You entered wrong password...")

    ## 3. Token expire time
    expire_time = datetime.utcnow() + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    print(expire_time)
    ## 4. Generate JWT Token
    token = jwt.encode({"_id":user.id, "exp":expire_time.timestamp()}, settings.SECRET_KEY,  settings.ALGORITHM)

    return {"token": token}
    

def is_authenticated(request:Request, db:Session):
    try:
        token = request.headers.get("authorization")
        print("trigger 1",token)
        if not token:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized...")
        
        print("trigger 2",token)
        ## 1. Decode JWT Token
        token = token.split(" ")[-1]
        print("trigger 3",token)
        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        print("trigger 4",data)
    
        ## 2. Check if user exists
        user_id = data.get("_id")
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized...")
        
        return user
    
    except InvalidTokenError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized...")



