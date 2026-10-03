from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User
from app.models.ride import Ride

from app.routes.users import router as users_router
from app.routes.rides import router as rides_router
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)
app.include_router(rides_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Carpool API running"}