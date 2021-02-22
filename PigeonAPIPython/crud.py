from sqlalchemy.orm import Session
import models, schemas
import bcrypt


def get_user_by_username(db: Session, username: str):
    return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.UserInfo(username=user.username, password=hashed_password, fullname=user.fullname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def check_username_password(db: Session, user: schemas.UserAuthenticate):
    db_user_info: models.UserInfo = get_user_by_username(db, username=user.username)
    return bcrypt.checkpw(user.password.encode('utf-8'), db_user_info.password.encode('utf-8'))


def create_new_sms(db: Session, sms: schemas.SMSBase):
    db_sms = models.SMS(
        company_uuid=sms.company_uuid,
        android_id=sms.android_id,
        from_number=sms.from_number,
        message=sms.message,
        to_number=sms.to_number
    )
    db.add(db_sms)
    db.commit()
    db.refresh(db_sms)
    return db_sms

def get_all_sms(db: Session):
    return db.query(models.SMS).all()

def get_all_sms_by_android_id(db: Session, android_id : str):
    return db.query(models.SMS).filter(models.SMS.android_id == android_id).all()