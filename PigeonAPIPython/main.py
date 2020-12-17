from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

import models, schemas, crud
from starlette import status
from database import engine, SessionLocal
from utils import decode_access_token
from crud import get_user_by_username
from database import engine, SessionLocal
from schemas import UserInfo, TokenData, UserCreate, Token

models.Base.metadata.create_all(bind=engine)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

TITLE = "Pigeon SMS Gateway API"
DESCRIPTION = "API Python to App Android Pigeon SMS Gateway."
VERSION = "0.0.1 Beta"
DOCS = "https://realmapp.com.br:8000/docs"
REDOC = "https://realmapp.com.br:8000/redoc"


app = FastAPI(title=TITLE, description=DESCRIPTION, version=VERSION)


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authenticate")


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(data=token)
        username: str = payload.get("sub")
        
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

@app.post("/user", response_model=schemas.UserInfo)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/authenticate", response_model=schemas.Token)
def authenticate_user(user: schemas.UserAuthenticate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Username not existed")
    else:
        is_password_correct = crud.check_username_password(db, user)
        if is_password_correct is False:
            raise HTTPException(status_code=400, detail="Password is not correct")
        else:
            from datetime import timedelta
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            from utils import create_access_token
            access_token = create_access_token(
                data={"sub": user.username}, expires_delta=access_token_expires)
            return {"access_token": access_token, "token_type": "Bearer"}


@app.get("/")
def read_root():
    return {
        "title": TITLE,
        "description": DESCRIPTION,
        "docs": DOCS,
        "redoc": REDOC,
        "version": VERSION,
    }

@app.get("/send")
def read_send(current_user: UserInfo = Depends(get_current_user), db: Session = Depends(get_db)):
    response = crud.get_all_sms(db=db)
    return {
        "error": False,
        "response": response
    }

@app.get("/send/{android_id}")
def read_send(android_id: str, urrent_user: UserInfo = Depends(get_current_user), db: Session = Depends(get_db)):
    response = crud.get_all_sms_by_android_id(db=db, android_id=android_id)
    return {
        "error": False,
        "response": response
    }
    

@app.put("/status/{device_id}")
def write_status(device_id: str, message_uuid: str, status: int):
    return {"device_id": device_id, "message_uuid": message_uuid, "status": status}


@app.post("/receive/{device_id}")
def read_receive(device_id: str, number: int, message: str):
    return {"device_id": device_id, "number": number, "message": message}
