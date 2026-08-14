from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. The URL pointing to your Postgres database
# Format: postgresql://[user]:[password]@[host]:[port]/[database_name]
SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost:5433/medpulse_db"

# 2. The Engine (the physical bridge to the database)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. The Session (a temporary workspace for database tasks)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. The Dependency (gives each API call its own database connection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()