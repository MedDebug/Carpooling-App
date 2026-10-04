from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate

from app.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        college_email=user.college_email,
        phone=user.phone,
        branch=user.branch,
        degree=user.degree,
        division=user.division,
        year=user.year
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user