from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.user import User
from src.core.security import verify_password, hash_password
from src.dto.user import UserCreate


class CRUDUser(CRUDBase[User, UserCreate]):
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            email=obj_in.email,
            password=hash_password(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email_or_username(db, email_or_username=email)

        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None

        return user

    @staticmethod
    def get_by_email_or_username(db: Session, *, email_or_username: str) -> Optional[User]:
        return db.query(User).filter(
            (User.email == email_or_username) | (User.username == email_or_username)
        ).first()

    @staticmethod
    def is_active(user: User) -> bool:
        return user.is_active


user = CRUDUser(User)
