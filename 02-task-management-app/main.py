from fastapi import FastAPI
from src.utils.db import Base, engine
from src.user.router import user_routes
from src.tasks.router import task_routes


# Base.metadata.create_all(bind = engine) -> This will create all the tables in the database
Base.metadata.create_all(bind = engine)


app = FastAPI(title = "Task Management App", description = "This is my Task Management Application", version = "1.0.0")


# Including all the routes
app.include_router(task_routes)
app.include_router(user_routes)