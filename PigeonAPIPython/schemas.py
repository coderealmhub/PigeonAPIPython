from typing import List
from pydantic import BaseModel


class UserInfoBase(BaseModel):
    username: str


class UserCreate(UserInfoBase):
    fullname: str
    password: str


class UserAuthenticate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None


class SMSBase(BaseModel):
    uuid = str
    company_uuid = str
    android_id = str
    from_number = str
    message = str
    to_number = str
    created = str
    updated = str

class SMS(SMSBase):
    id: int

    class Config:
        orm_mode = True