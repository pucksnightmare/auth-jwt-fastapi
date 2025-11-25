from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate, UserPasswordUpdate
from app.core.security import hash_password, verify_password
from app.core.security import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

# Crear usuario
@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):

    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está en uso")

    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    new_user = User(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Ver datos del usuario actual
@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user

# Actualizar username y/o email
@router.put("/update", response_model=UserResponse)
def update_user(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if data.username:
        if db.query(User).filter(User.username == data.username).first():
            raise HTTPException(status_code=400, detail="Ese username ya está en uso")

        current_user.username = data.username

    if data.email:
        if db.query(User).filter(User.email == data.email).first():
            raise HTTPException(status_code=400, detail="Ese email ya está en uso")

        current_user.email = data.email

    db.commit()
    db.refresh(current_user)

    return current_user

# Cambiar contraseña
@router.put("/change-password")
def change_password(
    data: UserPasswordUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Validar contraseña actual
    if not verify_password(data.current_password, current_user.password_hash):
        raise HTTPException(status_code=400, detail="La contraseña actual es incorrecta")

    # Validar nueva contraseña (mínimo 8 chars, 1 número)
    new = data.new_password
    if len(new) < 8 or not any(c.isdigit() for c in new):
        raise HTTPException(
            status_code=400,
            detail="La nueva contraseña debe tener mínimo 8 caracteres y al menos un número"
        )

    # Guardar nuevo hash
    current_user.password_hash = hash_password(new)

    db.commit()

    return {"message": "Contraseña actualizada correctamente"}

@router.delete("/delete-account")
def delete_account(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db.delete(current_user)
    db.commit()

    return {"message": "Cuenta eliminada correctamente"}