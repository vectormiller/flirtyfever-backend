from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import user as UserService
from dto import user as UserDTO
from settings import settings

router = APIRouter()

@router.post(settings.ROOT_URL, tags=["user"])
async def create_user(data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{id}', tags=["user"])
async def get_user(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)

@router.put('/{id}', tags=["user"])
async def update_user(data: UserDTO.User = None, db: Session = Depends(get_db), id: int = None):
    return UserService.update_user(data, db, id)

@router.delete('/', tags=["user"])
async def remove_user(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove_user(id, db)