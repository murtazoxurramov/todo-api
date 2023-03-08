from fastapi import FastAPI

from routers.user import router as user_router


def register_routers(app: FastAPI, prefix: str) -> None:
    app.include_router(
        user_router,
        tags=['user'],
        prefix=prefix
    )
