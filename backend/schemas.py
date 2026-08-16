from pydantic import BaseModel
from datetime import date, time, datetime
from typing import Optional

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone_number: str
    email: str

class PatientResponse(BaseModel):
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
    patient_id: int
    appointment_date: date
    start_time: time
    end_time: time
    status: str = 'Scheduled'
    notes: str = None

class AppointmentResponse(BaseModel):
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
    appointment_id: int
    amount: float
    status: str = 'Unpaid'

class InvoiceResponse(BaseModel):
    id: int
    appointment_id: int
    amount: float
    status: str
    issued_at: datetime
    model_config = {"from_attributes": True}



class PatientUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None

class AppointmentUpdate(BaseModel):
    appointment_date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    status: Optional[str] = None
    notes: Optional[str] = None

class InvoiceUpdate(BaseModel):
    amount: Optional[float] = None
    status: Optional[str] = None