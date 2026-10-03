from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    college_email = Column(String, unique=True, nullable=False, index=True)
    phone = Column(String, nullable=False)

    password_hash = Column(String, nullable=False)

    branch = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    division = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())