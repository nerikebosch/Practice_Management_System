from fastapi import FastAPI, HTTPException
from schemas import PatientCreate, PatientResponse, AppointmentCreate, AppointmentResponse, InvoiceCreate, InvoiceResponse
from datetime import datetime

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


# Create a new patient
@app.post("/patients/", response_model=PatientResponse)
def create_patient(patient: PatientCreate):
    # Logic to create a patient in the database
    return PatientResponse(
        id=1,
        first_name=patient.first_name,
        last_name=patient.last_name,
        date_of_birth=patient.date_of_birth,
        gender=patient.gender,
        phone_number=patient.phone_number,
        email=patient.email,
        created_at=datetime.now()
    )


# Get all patients
@app.get("/patients/", response_model=list[PatientResponse])
def get_patients():
    # Logic to retrieve all patients from the database
    return [
        PatientResponse(
            id=1,
            first_name="John",
            last_name="Doe",
            date_of_birth=datetime(1990, 1, 1).date(),
            gender="Male",
            phone_number="123-456-7890",
            email="john.doe@example.com",
            created_at=datetime.now()
        )
    ]

# Get one patient
@app.get("/patients/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int):
    # Logic to retrieve a patient by ID from the database
    if patient_id != 1:
        raise HTTPException(status_code=404, detail="Patient not found")
    return PatientResponse(
        id=1,
        first_name="John",
        last_name="Doe",
        date_of_birth=datetime(1990, 1, 1).date(),
        gender="Male",
        phone_number="123-456-7890",
        email="john.doe@example.com",
        created_at=datetime.now()
    )


# appointments
# Create a new appointment
@app.post("/appointments/", response_model=AppointmentResponse)
def create_appointment(appointment: AppointmentCreate):
    # Logic to create an appointment in the database
    if appointment.patient_id != 1:
        raise HTTPException(status_code=404, detail="Patient not found")
    return AppointmentResponse(
        id=1,
        patient_id=appointment.patient_id,
        appointment_date=appointment.appointment_date,
        start_time=appointment.start_time,
        end_time=appointment.end_time,
        status=appointment.status,
        notes=appointment.notes,
        created_at=datetime.now()
    )

# Get all appointments
@app.get("/appointments/", response_model=list[AppointmentResponse])
def get_appointments():
    # Logic to retrieve all appointments from the database
    return [
        AppointmentResponse(
            id=1,
            patient_id=1,
            appointment_date=datetime(2024, 1, 1).date(),
            start_time=datetime(2024, 1, 1, 9, 0).time(),
            end_time=datetime(2024, 1, 1, 10, 0).time(),
            status="Scheduled",
            notes="Initial consultation",
            created_at=datetime.now()
        )
    ]

# Get one appointment
@app.get("/appointments/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int):
    # Logic to retrieve an appointment by ID from the database
    if appointment_id != 1:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return AppointmentResponse(
        id=1,
        patient_id=1,
        appointment_date=datetime(2024, 1, 1).date(),
        start_time=datetime(2024, 1, 1, 9, 0).time(),
        end_time=datetime(2024, 1, 1, 10, 0).time(),
        status="Scheduled",
        notes="Initial consultation",
        created_at=datetime.now()
    )


# invoices
# Create a new invoice
@app.post("/invoices/", response_model=InvoiceResponse)
def create_invoice(invoice: InvoiceCreate):
    # Logic to create an invoice in the database
    if invoice.appointment_id != 1:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return InvoiceResponse(
        id=1,
        appointment_id=invoice.appointment_id,
        amount=invoice.amount,
        status=invoice.status,
        issued_at=datetime.now()
    )

# Get all invoices
@app.get("/invoices/", response_model=list[InvoiceResponse])
def get_invoices():
    # Logic to retrieve all invoices from the database
    return [
        InvoiceResponse(
            id=1,
            appointment_id=1,
            amount=100.0,
            status="Unpaid",
            issued_at=datetime.now()
        )
    ]

# Get one invoice
@app.get("/invoices/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(invoice_id: int):
    # Logic to retrieve an invoice by ID from the database
    if invoice_id != 1:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return InvoiceResponse(
        id=1,
        appointment_id=1,
        amount=100.0,
        status="Unpaid",
        issued_at=datetime.now()
    )