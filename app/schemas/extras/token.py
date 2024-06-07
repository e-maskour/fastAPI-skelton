from pydantic import BaseModel
from ..responses.users import UserResponse

class Token(BaseModel):
    user: UserResponse
    access_token: str
    refresh_token: str
