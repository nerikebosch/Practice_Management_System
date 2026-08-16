from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

import schemas
import models
from database import get_db

# create router and set prefix
router = APIRouter(
    prefix="/appointments",
    tags=["appointments"]
)

# Create a new appointment
@router.post("/", response_model=schemas.AppointmentResponse)
def create_appointment(appointmnet: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    # Check if the patient exists
    patient = db.query(models.Patient).filter(models.Patient.id == appointmnet.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    new_appointment = models.Appointment(
        patient_id=appointmnet.patient_id,
        appointment_date=appointmnet.appointment_date,
        start_time=appointmnet.start_time,
        end_time=appointmnet.end_time,
        status=appointmnet.status,
        notes=appointmnet.notes
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


# Get all appointments
@router.get("/", response_model= schemas.AppointmentResponse)
def get_appointments(db: Session = Depends(get_db)):
    appointments = db.query(models.Appointment).all()
    return appointments


# Get an appointment with ID
@router.get("/{appointment_id}", response_model=schemas.AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment


# Delete appointment by ID
@router.delete("/{appointment_id}", response_model=schemas.AppointmentResponse)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    db.delete(appointment)
    db.commit()

    return appointment


# Update appointment
@router.put("/{appointment_id}", response_model=schemas.AppointmentResponse)
def update_appointment(appointment_id: int, updated_appointment: schemas.AppointmentUpdate, db: Session = Depends(get_db)):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    for key, value in updated_appointment.dict(exclude_unset=True).items():
        setattr(appointment, key, value)

    db.commit()
    db.refresh(appointment)

    return appointment

