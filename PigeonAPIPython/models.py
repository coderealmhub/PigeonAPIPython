from sqlalchemy import Column, Integer, String
from database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    fullname = Column(String, unique=True)



class SMS(Base):
    __tablename__ = "tbl_sms"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True)
    company_uuid = Column(String)
    android_id = Column(String, unique=True)
    from_number = Column(String)
    message = Column(String)
    to_number = Column(String)
    created = Column(String)
    updated = Column(String)

    