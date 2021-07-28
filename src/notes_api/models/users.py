from pydantic import BaseModel, Field, EmailStr

from ..settings import settings


class BaseUser(BaseModel):
    email: EmailStr = Field(..., title="Email пользователя")
    username: str = Field(
        ...,
        title="Имя пользователя",
        min_length=settings.username_min_length,
        max_length=settings.username_max_length
    )


class UserCreate(BaseUser):
    password: str = Field(..., title="Пароль пользователя")


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True
