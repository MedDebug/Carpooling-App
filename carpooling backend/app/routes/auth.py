import bcrypt

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate

from fastapi import HTTPException
from app.auth import create_access_token
from app.schemas.user import UserCreate, UserLogin
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    new_user = User(
        name=user.name,
        college_email=user.college_email,
        phone=user.phone,
        password_hash=hashed_password,
        branch=user.branch,
        degree=user.degree,
        division=user.division,
        year=user.year
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.college_email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    password_correct = bcrypt.checkpw(
        form_data.password.encode("utf-8"),
        db_user.password_hash.encode("utf-8")
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(db_user.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }