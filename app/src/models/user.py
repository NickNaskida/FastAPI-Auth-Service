from sqlalchemy import Column, Boolean, Integer, String

from src.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True)
    first_name = Column(String(25), index=True)
    last_name = Column(String(80), index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String())
    is_active = Column(Boolean, default=True)
