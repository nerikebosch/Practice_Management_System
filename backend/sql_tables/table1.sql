CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(15),
    phone_number VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS appointments (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Scheduled', -- e.g., Scheduled, Completed, Cancelled
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Relationship: If a patient is deleted, delete their appointments
    CONSTRAINT fk_patient
        FOREIGN KEY(patient_id) 
        REFERENCES patients(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS invoices (
    id SERIAL PRIMARY KEY,
    appointment_id INT NOT NULL UNIQUE, -- One invoice per appointment
    amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Unpaid', -- e.g., Unpaid, Paid
    issued_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Relationship: If an appointment is deleted, delete its invoice
    CONSTRAINT fk_appointment
        FOREIGN KEY(appointment_id) 
        REFERENCES appointments(id)
        ON DELETE CASCADE
);