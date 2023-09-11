import uvicorn
from fastapi import FastAPI

from database import Base, engine
from routers.user import router as UserRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserRouter, prefix="/user")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=2)
