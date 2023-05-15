import os
from sqlalchemy import create_engine


# Set the SQLite database filename
sqlite_filename = "local_database.db"

# SQLite URL connection string
SQLALCHEMY_DATABASE_URL = f"sqlite:///{sqlite_filename}"

# Instantiate database engine
Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Import the Base class and the metadata from your models
from app.models.database.database import Base
from app.models.database import article

# Create the tables if they do not exist
Base.metadata.create_all(bind=Engine)