from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.ride import Ride
from app.schemas.ride import RideCreate

router = APIRouter(prefix="/rides", tags=["Rides"])


@router.post("/")
def create_ride(ride: RideCreate, db: Session = Depends(get_db)):
    new_ride = Ride(
        driver_id=ride.driver_id,
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