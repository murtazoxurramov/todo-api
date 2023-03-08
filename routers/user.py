from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from mics.function import get_password_hash
from models.request.user import RegisterUser
from db.session import get_repo
from service.repo.repo import SQLAlchemyRepos
from service.repo.user_repo import UserRepo


router = APIRouter()


@router.post(
    path="/register",
    description="Register some new user"
)
async def register_user(
    user: RegisterUser,
    repo: SQLAlchemyRepos = Depends(get_repo)
):
    user_repo = repo.get_repo(UserRepo)
    if await user_repo.get_user(email=user.email) is None:
        await user_repo.add_user(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=get_password_hash(password=user.password)
        )
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={'detail': 'User created successfully!'}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'detail': 'User already registered'}
        )
