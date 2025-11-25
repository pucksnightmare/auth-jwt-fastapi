from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.core.security import hash_password
from app.core.security import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


# -----------------------------
# Crear usuario
# -----------------------------
@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    # Validar usuario existente
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está en uso")

    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    # Crear usuario
    new_user = User(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# -----------------------------
# Obtener usuario actual
# -----------------------------
@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user


# -----------------------------
# Actualizar usuario actual
# -----------------------------
@router.patch("/me", response_model=UserResponse)
def update_current_user(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if data.username:
        # Verificar si otro usuario ya usa ese username
        if db.query(User).filter(User.username == data.username, User.id != current_user.id).first():
            raise HTTPException(status_code=400, detail="Ese nombre de usuario ya está en uso")

        current_user.username = data.username

    if data.email:
        # Verificar si otro usuario ya usa ese email
        if db.query(User).filter(User.email == data.email, User.id != current_user.id).first():
            raise HTTPException(status_code=400, detail="Ese correo ya está registrado")

        current_user.email = data.email

    db.commit()
    db.refresh(current_user)

    return current_user
