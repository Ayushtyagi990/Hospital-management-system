from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from .model import Patient,Doctor,Department,Appointment, Discount,Hospital,Address,Billing,Staff,Ambulance,Supplier,pharmacy, Category, salary,Product, Prescription, PrescriptionMedicine, Bed,   Admission
from .database import get_session

app = FastAPI()

@app.post("/patient/")
def create_patient(patient :  Patient, session : Session = Depends(get_session)):
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

@app.get("/patient")
def get_patient(session : Session = Depends(get_session)):
    patient = session.exec(select(Patient)).all()
    return patient

@app.post("/Doctor")
def create_Doctor(Doctor :  Doctor, session : Session = Depends(get_session)):
    session.add(Doctor)
    session.commit()
    session.refresh(Doctor)
    return Doctor

@app.post("/Department")
def create_Department(Department : Department, session : Session = Depends(get_session)):
    session.add(Department)
    session.commit()
    session.refresh(Department)
    return Department
@app.post("/Appointment")
def create_Appointment(Appointment : Appointment, session : Session = Depends(get_session)):
    session.add(Appointment)
    session.commit()
    session.refresh(Appointment)
    return Appointment

@app.post("/Discount")
def create_supplier(Discount : Discount, session : Session = Depends(get_session)):
    session.add(Discount)
    session.commit()
    session.refresh(Discount)
    return Discount

@app.post("/Hospital")
def create_Hospital(Hospital : Hospital, session : Session = Depends(get_session)):
    session.add(Hospital)
    session.commit()
    session.refresh(Hospital)
    return Hospital
@app.post("/Address")
def create_Address(Address : Address, session : Session = Depends(get_session)):
    session.add(Address)
    session.commit()
    session.refresh(Address)
    return Address
@app.post("/Billing")
def create_Billing(Billing : Billing, session : Session = Depends(get_session)):
    session.add(Billing)
    session.commit()
    session.refresh(Billing)
    return Billing
@app.post("/staff")
def create_staff(staff : Staff, session : Session = Depends(get_session)):
    session.add(staff)
    session.commit()
    session.refresh(staff)
    return staff

@app.post("/Ambulance")
def create_Ambulance(Ambulance : Ambulance, session : Session = Depends(get_session)):
    session.add(Ambulance)
    session.commit()
    session.refresh(Ambulance)
    return Ambulance

@app.post("/supplier")
def create_supplier( supplier : Supplier, session : Session = Depends(get_session)):
    session.add(supplier)
    session.commit()
    session.refresh(supplier)
    return  supplier

@app.post("/pharmacy")
def create_pharmacy(pharmacy :pharmacy, session : Session = Depends(get_session)):
    session.add(pharmacy)
    session.commit()
    session.refresh(pharmacy)
    return pharmacy
@app.post("/Category")
def create_Category(Category :Category, session : Session = Depends(get_session)):
    session.add(Category)
    session.commit()
    session.refresh(Category)
    return Category
@app.post("/salary")
def create_salary(salary :salary, session : Session = Depends(get_session)):
    session.add(salary)
    session.commit()
    session.refresh(salary)
    return salary


@app.post("/product")
def create_product(product : Product, session : Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product




@app.post("/Prescription")
def create_Prescription(Prescription :Prescription, session : Session = Depends(get_session)):
    session.add(Prescription)
    session.commit()
    session.refresh(Prescription)
    return Prescription





@app.post("/PrescriptionMedicine")
def create_PrescriptionMedicine(PrescriptionMedicine :PrescriptionMedicine, session : Session = Depends(get_session)):
    session.add(PrescriptionMedicine)
    session.commit()
    session.refresh(PrescriptionMedicine)
    return PrescriptionMedicine




@app.post("/Bed")
def create_Bed(Bed :Bed, session : Session = Depends(get_session)):
    session.add(Bed)
    session.commit()
    session.refresh(Bed)
    return Bed




@app.post("/Admission")
def create_Admission(Admission : Admission, session : Session = Depends(get_session)):
    session.add( Admission)
    session.commit()
    session.refresh(Admission)
    return  Admission
