from fastapi import APIRouter, FastAPI
from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.database import User

app = FastAPI(
    docs_url="/",
    title="Apex_uni",
)

main_router = APIRouter(prefix="")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(main_router)