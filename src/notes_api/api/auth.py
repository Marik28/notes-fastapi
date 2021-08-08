from fastapi import (
    APIRouter,
    Depends,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm

from ..models.auth import Token
from ..models.responses import Message
from ..models.users import UserCreate, User
from ..services.auth import (
    AuthService,
    get_current_user,
)

router = APIRouter(
    prefix='/auth',
)


@router.post(
    '/sign-up/',
    response_model=Token,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "model": Message,
            "description": "User with provided credentials already exists",
        },
    },
)
def sign_up(
        user_data: UserCreate,
        auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=Token,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "model": Message,
            "description": "Incorrect credentials provided",
        },
    },
)
def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(),
):
    return auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )


@router.get(
    '/user/',
    response_model=User,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "model": Message,
            "description": "Error: Unauthorized",
        }
    }
)
def get_user(user: User = Depends(get_current_user)):
    return user
