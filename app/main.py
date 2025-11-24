# app/main.py
from fastapi import FastAPI
from app.db import init_db
from app.core.config import settings

def create_app():
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="API académica de autenticación JWT con FastAPI y SQLite"
    )

    @app.get("/ping", tags=["health"])
    def ping():
        return {"status": "ok"}

    return app

app = create_app()

@app.get("/", tags=["root"])
def root():
    return {"message": "API funcionando correctamente"}

@app.on_event("startup")
def on_startup():
    init_db()
