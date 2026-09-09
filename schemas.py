from pydantic import BaseModel
class EmployeeCreate(BaseModel):
  name:str
  age:int
  department:str
class Employee(EmployeeCreate):
    id: int
class Config:
        from_attributes = True   
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
