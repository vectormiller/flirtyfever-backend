"""
    Main Module - FastAPI Application Entry Point

    This module sets up the FastAPI app, includes routers, and runs the application using Uvicorn.

    Modules and Packages:
        - uvicorn: ASGI server used for running the FastAPI application.
        - FastAPI: Web framework used to create RESTful APIs.
        - database: Module for managing the database connection and ORM.
        - routers.user: Router module for user-related API endpoints.

    Usage:
        To start the FastAPI application, run this module as the main script. It will launch the web server
        on the specified host and port.

    Example:
        python main.py

    Configuration:
        You can configure the host, port, and other settings by modifying the `uvicorn.run` call at the end of this script.
"""

import uvicorn
from fastapi import FastAPI

from database import Base, engine
from routers.user import router as UserRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserRouter, prefix="/user")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=2)
