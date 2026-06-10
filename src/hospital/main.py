from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from .model import Patient,Doctor,Department,Appointment, Discount,Hospital,Address,Billing,Staff,Ambulance,Supplier,Pharmacy, Category, Salary,Product, Prescription, PrescriptionMedicine, Bed,   Admission
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

@app.delete("/patient", status_code = 204)
def create_patient(session : Session = Depends(get_session)):
    patient = session.exec(select(Patient)).all()
    for patient in patient : 
        session.delete(patient)
        session.commit()
    return {"details" :  "all patient is delete"}


@app.post("/Doctor")
def create_Doctor(Doctor :  Doctor, session : Session = Depends(get_session)):
    session.add(Doctor)
    session.commit()
    session.refresh(Doctor)
    return Doctor

@app.get("/Doctor")
def get_Doctor(session : Session = Depends(get_session)):
    doctor = session.exec(select(Doctor)).all()
    return doctor



@app.delete("/Doctor", status_code = 204)
def create_Doctor(session : Session = Depends(get_session)):
    doctor = session.exec(select(Doctor)).all()
    for doctor in doctor : 
        session.delete(doctor)
        session.commit()
    return {"details" :  "all Doctor is delete"}

@app.post("/Department")
def create_Department(Department : Department, session : Session = Depends(get_session)):
    session.add(Department)
    session.commit()
    session.refresh(Department)
    return Department

@app.delete("/Department", status_code = 204)
def create_Department(session : Session = Depends(get_session)):
    department = session.exec(select(Department)).all()
    for department in department : 
        session.delete(department)
        session.commit()
    return {"details" :  "all Department is delete"}

@app.post("/Appointment")
def create_Appointment(Appointment : Appointment, session : Session = Depends(get_session)):
    session.add(Appointment)
    session.commit()
    session.refresh(Appointment)
    return Appointment


@app.delete("/Appointment", status_code = 204)
def create_Appointment(session : Session = Depends(get_session)):
    appointment = session.exec(select(Appointment)).all()
    for appointment in appointment : 
        session.delete(appointment)
        session.commit()
    return {"details" :  "all Appointment is delete"}  


@app.post("/Discount")
def create_supplier(Discount : Discount, session : Session = Depends(get_session)):
    session.add(Discount)
    session.commit()
    session.refresh(Discount)
    return Discount

@app.delete("/Discount", status_code = 204)
def create_Discount(session : Session = Depends(get_session)):
    discount = session.exec(select(Discount)).all()
    for discount in discount : 
        session.delete(discount)
        session.commit()
    return {"details" :  "all Discount is delete"}  


@app.post("/Hospital")
def create_Hospital(Hospital : Hospital, session : Session = Depends(get_session)):
    session.add(Hospital)
    session.commit()
    session.refresh(Hospital)
    return Hospital


@app.delete("/Hospital", status_code = 204)
def create_Hospital(session : Session = Depends(get_session)):
    hospital = session.exec(select(Hospital)).all()
    for hospital in hospital : 
        session.delete(hospital)
        session.commit()
    return {"details" :  "all Hospital is delete"}  


@app.post("/Address")
def create_Address(address : Address, session : Session = Depends(get_session)):
    session.add(address)
    session.commit()
    session.refresh(address)
    return address


@app.get("/address")
def get_address(session : Session = Depends(get_session)):
    address = session.exec(select(Address)).all()
    return address


@app.delete("/address", status_code = 204)
def create_address(session : Session = Depends(get_session)):
    address = session.exec(select(Address)).all()
    for address in address : 
        session.delete(address)
        session.commit()
    return {"details" :  "all address is delete"}

@app.post("/Billing")
def create_Billing(Billing : Billing, session : Session = Depends(get_session)):
    session.add(Billing)
    session.commit()
    session.refresh(Billing)
    return Billing

@app.delete("/Billing", status_code = 204)
def create_Billing(session : Session = Depends(get_session)):
    billing = session.exec(select(Billing)).all()
    for billing in billing : 
        session.delete(billing)
        session.commit()
    return {"details" :  "all billing is delete"}


@app.post("/staff")
def create_staff(staff : Staff, session : Session = Depends(get_session)):
    session.add(staff)
    session.commit()
    session.refresh(staff)
    return staff


@app.delete("/staff", status_code = 204)
def create_staff(session : Session = Depends(get_session)):
    staff = session.exec(select(Staff)).all()
    for staff in staff : 
        session.delete(staff)
        session.commit()
    return {"details" :  "all staff is delete"}


@app.post("/Ambulance")
def create_Ambulance(Ambulance : Ambulance, session : Session = Depends(get_session)):
    session.add(Ambulance)
    session.commit()
    session.refresh(Ambulance)
    return Ambulance

@app.delete("/Ambulance", status_code = 204)
def create_Ambulance(session : Session = Depends(get_session)):
    ambulance = session.exec(select(Ambulance)).all()
    for ambulance in ambulance: 
        session.delete(ambulance)
        session.commit()
    return {"details" :  "all Ambulance is delete"}


@app.post("/supplier")
def create_supplier(supplier : Supplier, session : Session = Depends(get_session)):
    session.add(supplier)
    session.commit()
    session.refresh(supplier)
    return  supplier


@app.delete("/supplier", status_code = 204)
def create_supplier(session : Session = Depends(get_session)):
    supplier = session.exec(select(Supplier)).all()
    for supplier in supplier: 
        session.delete(supplier)
        session.commit()
    return {"details" :  "all supplier is delete"}


@app.post("/pharmacy")
def create_pharmacy(pharmacy : Pharmacy, session : Session = Depends(get_session)):
    session.add(pharmacy)
    session.commit()
    session.refresh(pharmacy)
    return pharmacy


@app.delete("/pharmacy", status_code = 204)
def create_pharmacy(session : Session = Depends(get_session)):
    pharmacy = session.exec(select(Pharmacy)).all()
    for pharmacy in pharmacy: 
        session.delete(pharmacy)
        session.commit()
    return {"details" :  "all pharmacy is delete"}


@app.post("/Category")
def create_Category(Category :Category, session : Session = Depends(get_session)):
    session.add(Category)
    session.commit()
    session.refresh(Category)
    return Category

@app.delete("/Category", status_code = 204)
def create_Category(session : Session = Depends(get_session)):
    category = session.exec(select(Category)).all()
    for category in category: 
        session.delete(category)
        session.commit()
    return {"details" :  "all Category  is delete"}


@app.post("/salary")
def create_salary(salary : Salary, session : Session = Depends(get_session)):
    session.add(salary)
    session.commit()
    session.refresh(salary)
    return salary

@app.delete("/salary", status_code = 204)
def create_salary(session : Session = Depends(get_session)):
    salary = session.exec(select(Salary)).all()
    for salary in salary: 
        session.delete(salary)
        session.commit()
    return {"details" :  "all salary is delete"}


@app.post("/product")
def create_product(product : Product, session : Session = Depends(get_session)):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@app.delete("/product", status_code = 204)
def create_product(session : Session = Depends(get_session)):
    product = session.exec(select(Product)).all()
    for product in product: 
        session.delete(product)
        session.commit()
    return {"details" :  "all product is delete"}





@app.post("/Prescription")
def create_Prescription(Prescription :Prescription, session : Session = Depends(get_session)):
    session.add(Prescription)
    session.commit()
    session.refresh(Prescription)
    return Prescription

@app.delete("/Prescription", status_code = 204)
def create_salary(session : Session = Depends(get_session)):
    prescription = session.exec(select(Prescription)).all()
    for prescription in prescription: 
        session.delete(prescription)
        session.commit()
    return {"details" :  "all prescription is delete"}



@app.post("/PrescriptionMedicine")
def create_PrescriptionMedicine(PrescriptionMedicine :PrescriptionMedicine, session : Session = Depends(get_session)):
    session.add(PrescriptionMedicine)
    session.commit()
    session.refresh(PrescriptionMedicine)
    return PrescriptionMedicine




@app.delete("/PrescriptionMedicine", status_code = 204)
def create_PrescriptionMedicine(session : Session = Depends(get_session)):
    prescriptionMedicine = session.exec(select(PrescriptionMedicine)).all()
    for prescriptionMedicine in prescriptionMedicine: 
        session.delete(prescriptionMedicine)
        session.commit()
    return {"details" :  "all prescriptionMedicine is delete"}




@app.post("/Bed")
def create_Bed(Bed :Bed, session : Session = Depends(get_session)):
    session.add(Bed)
    session.commit()
    session.refresh(Bed)
    return Bed


@app.delete("/Bed", status_code = 204)
def create_Bed(session : Session = Depends(get_session)):
    bed= session.exec(select(Bed)).all()
    for  bed in bed: 
        session.delete(bed)
        session.commit()
    return {"details" :  "all bed is delete"}



@app.post("/Admission")
def create_Admission(Admission : Admission, session : Session = Depends(get_session)):
    session.add( Admission)
    session.commit()
    session.refresh(Admission)
    return  Admission



@app.delete("/Admission", status_code = 204)
def create_Admission(session : Session = Depends(get_session)):
    admission= session.exec(select(Admission)).all()
    for  admission in admission : 
        session.delete(admission)
        session.commit()
    return {"details" :  "all admission is delete"}


