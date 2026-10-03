from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database import Base


class Ride(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)

    driver_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)

    departure_time = Column(DateTime, nullable=False)

    available_seats = Column(Integer, nullable=False)

    status = Column(String, default="active")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )