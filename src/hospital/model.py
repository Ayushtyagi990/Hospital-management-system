from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, date, time


class Address(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    city : str | None = Field(default  = None)
    state : str | None = Field(default  = None)
    country : str | None = Field(default  = None)
    pincode : int | None = Field(default  = None)
    latitude : float | None = Field(default  = None)
    longitude : float |  None = Field(default = None)


class Hospital(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    type : str | None = Field(default  = None)
    phone : str | None = Field(default  = None)
    email : str | None = Field(index = True, unique = True)
    address_id : int | None = Field(default = None, foreign_key = "address.id")
    address : Address | None = Relationship()
    total_beds : int | None = Field(default = None)
    available_beds : int | None = Field(default = None)
    emergency_available: str | None = Field(default = None)


class Patient(SQLModel, table= True):
    id : int | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    age : int | None = Field(default = None)
    gender : str | None = Field(default = None)
    phone : str | None = Field(default = None)
    email  : str |  None = Field(index = True, unique = True)
    address : str | None = Field(default = None)
    blood_group : str | None = Field(default = None)
    registration_date : datetime | None = Field(default = None)


class Department(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    description :str | None = Field(default = None)


class Doctor(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    age : int | None = Field(default = None)
    gender : str | None = Field(default = None)
    phone : str | None = Field(default = None)
    email  : str |  None = Field(index =  True, unique = True)
    address : str | None = Field(default = None)
    specialization : str | None = Field(default  = None)
    department : int | None = Field(default = None, foreign_key = "department.id")
    department  : Department | None = Relationship()


class Appointment(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    patient_id : int | None = Field(default = None, foreign_key = "patient.id")
    patient : Patient | None = Relationship()
    doctor_id : int | None = Field(default  = None, foreign_key = "doctor.id")
    doctor : Doctor | None = Relationship()
    appointment_date: date | None = Field(default = None)
    appointment_time : time | None = Field(default = None)
    status : str | None = Field(default = None)


class Discount(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    patient_id : int | None = Field(default = None, foreign_key = "patient.id")
    patient : Patient | None = Relationship()
    doctor_id : int | None = Field(default  = None, foreign_key = "doctor.id")
    doctor : Doctor | None = Relationship()
    discount_percent: float | None = Field(default = None)


class Category(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str | None =  Field(default = None)


class Billing(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    patient_id : int | None = Field(default = None, foreign_key = "patient.id")
    patient : Patient | None = Relationship()
    doctor_id : int | None = Field(default  = None, foreign_key = "doctor.id")
    doctor : Doctor | None = Relationship()
    appointment_id : int | None = Field(default = None)
    total_amount : int | None = Field(default = None)
    payment_method : str | None = Field(default = None)
    payment_status : str | None = Field(default = None)
    billing_date   : datetime| None = Field(default = None)


class Staff(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str | None =  Field(default = None)
    phone : str | None =  Field(default = None) 
    email : str | None = Field(index = True, unique = True)
    duty_time : datetime | None = Field(default  = None)


class salary(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    staff_id : int| None = Field(default = None, foreign_key = "staff.id")
    staff : Staff | None = Relationship()
    amount : int | None = Field(default = None)
    pf : float | None = Field(default  = None)
    house_allowence  : float | None = Field(default = None)
    basic_salary : float  | None = Field (default  = None)
    tds_deduction : float | None = Field(default = None)


class Ambulance(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    number : int | None = Field(default = None)
    driver_name : str | None = Field(default = None)
    phone : str | None = Field(default  = None)
    status : str | None = Field(default  = None)

class Supplier(SQLModel, table = True):
    id : int | None = Field(default  = None, primary_key = True)
    name : str | None = Field(default = None)
    phone : str | None  = Field(default = None)
    address: str | None = Field(default = None)


class Product(SQLModel, table = True):
    id : int | None  = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    base_price : int | None = Field(default = None)
    tax_price : int | None = Field(default =  None)
    net_price : int | None = Field(default =  None)
    quanitiy : float | None = Field(default = None)
    supplier_id  : int | None = Field(default = None, foreign_key = "supplier.id")
    supplier : Supplier | None = Relationship()


class pharmacy(SQLModel, table = True):
    id : int | None = Field(default = None, primary_key = True)
    name : str | None = Field(default = None)
    category_id : int | None = Field(default = None, foreign_key = "category.id")
    category : Category | None = Relationship()
    stock_quantity : int | None = Field(default = None)
    expiry_date : datetime | None = Field(default = None)
    supplier_date : datetime | None = Field(default = None)

class Prescription(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    patient_id: int = Field(default = None, foreign_key="patient.id")
    patient : Patient | None = Relationship()
    doctor_id: int = Field(default = None,foreign_key="doctor.id")
    doctor : Doctor | None = Relationship()
    date: datetime | None = Field(default = None)

class Prescription_Medicine(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    prescription_id: int = Field(default = None, foreign_key="prescription.id")
    prescription : Prescription | None = Relationship()
    medicine_name: str | None = Field(default =  None)
    dosage: str | None  = Field(default  = None)
    duration: str | None = Field(default = None)

class Bed(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hospital_id: int = Field(default = None, foreign_key="hospital.id")
    hospital : Hospital | None = Relationship()
    bed_number: str = Field(default = None)
    status: str = Field(default  = None)

class Admission(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    patient_id: int = Field(default = None, foreign_key="patient.id")
    patient : Patient | None = Relationship()
    bed_id: int = Field(default = None, foreign_key="bed.id")
    bed : Bed | None = Relationship()
    admission_date: datetime | None = Field(default = None)
    discharge_date: datetime | None = Field(default = None)