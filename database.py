from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from passlib.hash import bcrypt  
import os

dirname = os.path.dirname(__file__)
db_path = os.path.join(dirname, 'mydatabase.db')

engine = create_engine(f'sqlite:///{db_path}', connect_args={"check_same_thread": False}, echo=True)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)  

    def set_password(self, password: str):
        self.password = bcrypt.hash(password) 
Base.metadata.create_all(engine)
