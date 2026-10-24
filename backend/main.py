"""
This is the main entry point for the FastAPI application.
It sets up the FastAPI app, configures CORS, and includes the routers for patients, appointments, and invoices.
"""
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware, FastAPI

# Import your new router
from routers import patients
from routers import appointments
from routers import invoices

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add this CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # This is Angular's default port
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allows all headers
)

# Plug the router into the main app
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(invoices.router)

@app.get("/")
def root():
    """
    Root endpoint of the API.
    Returns a welcome message.
    """
    return {"message": "Welcome to the MedPulse API"}
