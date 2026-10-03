from datetime import datetime

from pydantic import BaseModel


class RideCreate(BaseModel):
    driver_id: int
    origin: str
    destination: str
    departure_time: datetime
    available_seats: int