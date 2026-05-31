import jwt 
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from fastapi import Request, HTTPException, status, Depends

## is_authenticated
def is_authenticated(request:Request, db:Session = Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized...")
        
        ## 1. Decode JWT Token
        token = token.split(" ")[-1]
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    
        ## 2. Check if user exists
        user_id = data.get("_id")
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized...")
        
        return user
    
    except InvalidTokenError as e:
        print("JWT Decode Error:", e)
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized...")
