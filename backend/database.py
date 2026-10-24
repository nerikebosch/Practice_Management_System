"""This module sets up the database connection 
nd session management for the FastAPI application.
It uses SQLAlchemy to connect to a PostgreSQL database 
and provides a session factory for creating database sessions.
The get_db function is a dependency that provides 
a database session for each API request.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost:5433/medpulse_db"

# The Engine (the physical bridge to the database)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# The Session (a temporary workspace for database tasks)
SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The Dependency (gives each API call its own database connection)
def get_db():
    """
    Dependency that provides a database session for each API request.
    Yields:
        Session: A SQLAlchemy database session.
    """
    db = SESSIONLOCAL()
    try:
        yield db
    finally:
        db.close()
