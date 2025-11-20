from fastapi import FastAPI
from app.db import init_db

def create_app():
    app = FastAPI(
        title="Auth JWT FastAPI",
        description="API académica para demostrar autenticación JWT con FastAPI y SQLite",
        version="1.0.0",
    )

    @app.get("/ping", tags=["health"])
    def ping():
        return {"status": "ok"}

    return app

app = create_app()

@app.on_event("startup")
def on_startup():
    # Inicializa la base de datos (crea tablas)
    init_db()
