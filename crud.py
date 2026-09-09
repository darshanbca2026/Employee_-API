from sqlalchemy.orm import Session
import model
from security import hash_password
import schemas
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = model.Employee(
    name=employee.name,
    age=employee.age,
    department = employee.department
)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
    def get_employees(db: Session):
     return db.query(model.Employee).all()
def get_employee(db: Session, employee_id: int):
 return db.query(model.Employee).filter(model.Employee.id == employee_id).first()
def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(model.Employee).filter(
        model.Employee.id == employee_id
    ).first()

    if db_employee is None:
        return None

    db_employee.name = employee.name
    db_employee.age = employee.age

    db.commit()
    db.refresh(db_employee)

    return db_employee                                                              

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(model.Employee).filter(model.Employee.id == employee_id).first()
    if db_employee is None:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee  # <-- add this so main.py knows it worked
def create_user(db, user):
    db_user = model.User(
        username=user.username,
        password = hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user  


