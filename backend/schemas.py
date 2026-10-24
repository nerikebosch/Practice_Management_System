"""
Schemas for the Practice Management System API.
This module defines the Pydantic models used for request and response validation in the API.
"""

from datetime import date, time, datetime
from typing import Optional
from pydantic import BaseModel

class PatientCreate(BaseModel):
    """
    Schema for creating a new patient.
    """
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone_number: str
    email: str

class PatientResponse(BaseModel):
    """
    Schema for returning patient information in API responses.
    """
    id: int
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone_number: str
    email: str
    created_at: datetime
    model_config = {"from_attributes": True}

class AppointmentCreate(BaseModel):
    """
    Schema for creating a new appointment.
    """
    patient_id: int
    appointment_date: date
    start_time: time
    end_time: time
    status: str = 'Scheduled'
    notes: str = None

class AppointmentResponse(BaseModel):
    """
    Schema for returning appointment information in API responses.
    """
    id: int
    patient_id: int
    appointment_date: date
    start_time: time
    end_time: time
    status: str
    notes: str = None
    created_at: datetime
    model_config = {"from_attributes": True}

class InvoiceCreate(BaseModel):
    """
    Schema for creating a new invoice.
    """
    appointment_id: int
    amount: float
    status: str = 'Unpaid'

class InvoiceResponse(BaseModel):
    """
    Schema for returning invoice information in API responses.
    """
    id: int
    appointment_id: int
    amount: float
    status: str
    issued_at: datetime
    model_config = {"from_attributes": True}

class PatientUpdate(BaseModel):
    """
    Schema for updating patient information.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None

class AppointmentUpdate(BaseModel):
    """
    Schema for updating appointment information.
    """
    appointment_date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    status: Optional[str] = None
    notes: Optional[str] = None

class InvoiceUpdate(BaseModel):
    """
    Schema for updating invoice information.
    """
    amount: Optional[float] = None
    status: Optional[str] = None
