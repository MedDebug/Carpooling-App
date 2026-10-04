from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    college_email: str
    phone: str
    password: str
    branch: str
    degree: str
    division: str
    year: int


class UserLogin(BaseModel):
    college_email: str
    password: str