from pydantic import UUID4, BaseModel, Field


class UserResponse(BaseModel):
    email: str = Field(..., example="emaskour@example.com")
    username: str = Field(..., example="Mask$&12")
    uuid: UUID4 = Field(..., example="a3b8f042-1e16-4f0a-a8f0-421e16df0a2f")
    is_admin: bool = Field(..., example=False)
    
    class Config:
        orm_mode = True
