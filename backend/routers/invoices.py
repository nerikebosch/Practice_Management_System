"""
This module contains the API routes for managing invoices in the database.
It provides endpoints for creating, retrieving, updating, and deleting invoice records.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
import models
from database import get_db

# create router and prefix
router = APIRouter(
    prefix="/invoices",
    tags=["invoices"]
)


# Create a new invoice
@router.post("/", response_model=schemas.InvoiceResponse)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    """
    Create a new invoice in the database.
    """
    # Check if the appointment exists
    appointment = db.query(models.Appointment).filter(models.Appointment.id ==
                                                      invoice.appointment_id).first()
    
    if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
    
    if invoice.appointment_id != 1:
        raise HTTPException(status_code=404, detail="Appointment not found")

    new_invoice = models.Invoice(
        appointment_id=invoice.appointment_id,
        amount=invoice.amount,
        status=invoice.status,
        issued_at=invoice.issued_at
    )

    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)

    return new_invoice


# Get all invoices
@router.get("/", response_model=list[schemas.InvoiceResponse])
def get_invoices(db: Session = Depends(get_db)):
    """
    Get all invoices from the database.
    """
    invoices = db.query(models.Invoice).all()

    return invoices


# Get a invoice with ID
@router.get("/{invoice_id}", response_model=schemas.InvoiceResponse)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    """
    Get an invoice by ID from the database.
    """
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    return invoice


# Delete an invoice by ID
@router.delete("/{invoice_id}", response_model=schemas.InvoiceResponse)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    """
    Delete an invoice by ID from the database.
    """
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    db.delete(invoice)
    db.commit()

    return invoice


# Update invoice
@router.put("/{invoice_id}", response_model=schemas.InvoiceResponse)
def update_invoice(invoice_id: int, updated_invoice: schemas.InvoiceUpdate,
                   db: Session = Depends(get_db)):
    """
    Update an invoice by ID in the database.
    """
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    for key, value in updated_invoice.dict(exclude_unset=True).items():
        setattr(invoice, key, value)

    db.commit()
    db.refresh(invoice)

    return invoice
