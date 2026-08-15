from fastapi import FastAPI
import models
from database import engine

# Import your new router
from routers import patients

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Plug the router into the main app
app.include_router(patients.router)

@app.get("/")
def root():
    return {"message": "Welcome to the MedPulse API"}