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

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add this CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # This is Angular's default port
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)

# Your app.include_router(...) lines stay down here!

# Plug the router into the main app
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(invoices.router)

@app.get("/")
def root():
    return {"message": "Welcome to the MedPulse API"}

