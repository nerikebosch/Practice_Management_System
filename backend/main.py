from fastapi import FastAPI
import models
from database import engine

# Import your new router
from routers import patients
from routers import appointments
from routers import invoices

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Plug the router into the main app
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(invoices.router)

@app.get("/")
def root():
    return {"message": "Welcome to the MedPulse API"}