# This file will be used to create the connection between the application and the database

# declarative_base - It is used to create the base class for all the models
# sessionmaker - It is used to create a session with the database
# create_engine - It is used to create the connection between the application and the database

from sqlalchemy import create_engine
from src.utils.settings import settings
from sqlalchemy.orm import sessionmaker, declarative_base

# Base - It is the base class for all the models
Base = declarative_base()

# create_engine - It is used to create the connection between the application and the database
engine = create_engine(settings.DB_CONNECTION_STRING)

# LocalSession - It is used to create a session with the database
LocalSession = sessionmaker(bind=engine)

# get_db - It is used to get the connection to the database
def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()