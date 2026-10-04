from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.ride import Ride
from app.schemas.ride import RideCreate

from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/rides", tags=["Rides"])

@router.post("/")
def create_ride(
    ride: RideCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_ride = Ride(
        driver_id=current_user.id,
        origin=ride.origin,
        destination=ride.destination,
        departure_time=ride.departure_time,
        available_seats=ride.available_seats
    )

    db.add(new_ride)
    db.commit()
    db.refresh(new_ride)

    return new_ride

@router.get("/")
def get_rides(db: Session = Depends(get_db)):
    rides = db.query(Ride).filter(Ride.status == "active").all()
    return rides