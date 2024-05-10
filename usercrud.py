from sqlalchemy.orm import Session
from database import User  
from cachetools import cached, TTLCache


cache = TTLCache(maxsize=1000, ttl=300)

@cached(cache)
def create_user(db: Session, name: str, password: str):
    db_user = User(name=name)
    db_user.set_password(password)  
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@cached(cache)
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
    
@cached(cache)
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.name == username).first()
            
@cached(cache)
def update_user(db: Session, user_id: int, name: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = name
    db.commit()
    db.refresh(db_user)
    return db_user

def search_users(db: Session, name: str):
    return db.query(User).filter(User.name.ilike(f"%{name}%")).all()
