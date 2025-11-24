# app/main.py

from fastapi import FastAPI
from app.db import init_db
from app.core.config import settings

from app.routers.auth import router as auth_router
from app.routers.user import router as user_router


def create_app():
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="API académica de autenticación JWT con FastAPI y SQLite"
    )

    app.include_router(auth_router)
    app.include_router(user_router)

    @app.get("/ping", tags=["health"])
    def ping():
        return {"status": "ok"}

    return app


app = create_app()


@app.on_event("startup")
def on_startup():
    init_db()
