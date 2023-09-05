from models.user import User
from sqlalchemy.orm import Session
from dto import user as UserDTO

def create_user(data: UserDTO.User, db: Session):
    user = User(
        name = data.name,
        lastname = data.lastname,
        middlename = data.middlename
    )
    try:
        db.add(user)
        db.commit()
        db.refresh
    except Exception as e:
        print(e)
    return user.id

def get_user(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()

def update_user(data: UserDTO.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    user.name = data.name
    user.lastname = data.lastname
    user.middlename = data.middlename

    db.add(user)
    db.commit()
    db.refresh(user)

def remove_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user
