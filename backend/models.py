from sqlalchemy import Column, Integer, String, Float, Date, Time, DateTime, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    appointments = relationship('Appointment', back_populates='patient')


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(String, default='Scheduled')
    notes = Column(String, nullable=True)

    patient = relationship('Patient', back_populates='appointments')
    invoices = relationship('Invoice', back_populates='appointment')

class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default='Unpaid')
    issued_at = Column(DateTime, nullable=True)

    appointment = relationship('Appointment', back_populates='invoices')
