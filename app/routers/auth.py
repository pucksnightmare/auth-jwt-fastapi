from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    # Buscar usuario por username
    user = db.query(User).filter(User.username == data.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario no encontrado",
        )

    # Verificar password
    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contraseña incorrecta",
        )

    # Crear token JWT con el username en el "sub"
    token = create_access_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer",
    }
