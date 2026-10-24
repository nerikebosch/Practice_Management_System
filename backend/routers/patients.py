"""
This module contains the API routes for managing patients in the database.
It provides endpoints for creating, retrieving, updating, and deleting patient records.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

# create router and set prefix
router = APIRouter(
    prefix="/patients",
    tags=["patients"]
)


# Create a new patient
@router.post("/", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    """
    Create a new patient in the database.
    """
    # Check if the email already exists in the database
    db_patient = db.query(models.Patient).filter(models.Patient.email == patient.email).first()
    
    # If it does exist, throw a clean 400 Bad Request error
    if db_patient:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_patient = models.Patient(
        first_name=patient.first_name,
        last_name=patient.last_name,
        date_of_birth=patient.date_of_birth,
        gender=patient.gender,
        phone_number=patient.phone_number,
        email=patient.email
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


# Get all the patients
@router.get("/", response_model=list[schemas.PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    """
    Get all patients from the database.
    """
    patients = db.query(models.Patient).all()

    return patients


# Get patient by ID
@router.get("/{patient_id}", response_model=schemas.PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    """
    Get a patient by ID from the database.
    """
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return patient


# Delete a patient by ID
@router.delete("/{patient_id}", response_model=schemas.PatientResponse)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    """
    Delete a patient by ID from the database.
    """
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(patient)
    db.commit()

    return patient


# Update patient information
@router.put("/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(patient_id: int, updated_patient: schemas.PatientUpdate, db: Session = Depends(get_db)):
    """
    Update a patient's information by ID.
    """
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    for key, value in updated_patient.dict(exclude_unset=True).items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)

    return patient
