from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Set the SQLite database filename
sqlite_filename = "local_database.db"

# SQLite URL connection string
SQLALCHEMY_DATABASE_URL = f"sqlite:///{sqlite_filename}"

# Instantiate database engine and session
Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Session = SessionLocal()

Base = declarative_base()