from pydantic import BaseModel
from typing import Optional

fake_users_db = {}

class User(BaseModel):
    username: str
    email: Optional[str] = None
    hashed_password: str


class UserInDB(User):
    hashed_password: str