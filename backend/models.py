# pylint: disable=too-few-public-methods

"""
This module defines the SQLAlchemy models for the application.
It includes the Patient, Appointment, and 
Invoice models, which represent the corresponding tables in the database
"""
from sqlalchemy import Column, Integer, String, Float, Date, Time, DateTime, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models.
    This class serves as the base for all SQLAlchemy models in the application.
    It provides the necessary metadata and configuration 
    for the models to be mapped to the database tables.
    """

class Patient(Base):
    """
    Patient model representing a patient in the database.
    Attributes:
        id (int): Unique identifier for the patient.
        first_name (str): First name of the patient.
        last_name (str): Last name of the patient.
        date_of_birth (date): Date of birth of the patient.
        gender (str): Gender of the patient.
        phone_number (str): Phone number of the patient.
        email (str): Email address of the patient.
        created_at (datetime): Timestamp when the patient was created.
        appointments (list): List of appointments associated with the patient.
    """
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, server_default='now()')

    appointments = relationship('Appointment', back_populates='patient')

class Appointment(Base):
    """
    Appointment model representing an appointment in the database.
    Attributes:
        id (int): Unique identifier for the appointment.
        patient_id (int): ID of the patient associated with the appointment.
        appointment_date (date): Date of the appointment.
        start_time (time): Start time of the appointment.
        end_time (time): End time of the appointment.
        status (str): Status of the appointment.
        notes (str): Additional notes for the appointment.
        created_at (datetime): Timestamp when the appointment was created.
        patient (Patient): The patient associated with the appointment.
        invoices (list): List of invoices associated with the appointment.
    """
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(String, default='Scheduled')
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default='now()')

    patient = relationship('Patient', back_populates='appointments')
    invoices = relationship('Invoice', back_populates='appointment')

class Invoice(Base):
    """
    Invoice model representing an invoice in the database.
    Attributes:
        id (int): Unique identifier for the invoice.
        appointment_id (int): ID of the appointment associated with the invoice.
        amount (float): The amount of the invoice.
        status (str): Status of the invoice.
        issued_at (datetime): Timestamp when the invoice was issued.
        appointment (Appointment): The appointment associated with the invoice.
    """
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default='Unpaid')
    issued_at = Column(DateTime, nullable=True)

    appointment = relationship('Appointment', back_populates='invoices')
