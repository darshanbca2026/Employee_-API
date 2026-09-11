README.MD
markdown# Employee Management API

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)](https://www.postgresql.org/)
[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-black)](https://render.com)

A secure and scalable RESTful API for Employee Management with JWT authentication, built using FastAPI and PostgreSQL.

**Live API:** https://employee-api-93no.onrender.com
**Swagger Docs:** https://employee-api-93no.onrender.com/docs

## Features

- JWT based Authentication and Authorization
- User Registration and Login
- Complete Employee CRUD Operations
- PostgreSQL with SQLAlchemy ORM
- Password Hashing with Bcrypt
- Auto-generated Interactive API Docs
- Docker and Docker Compose Support
- Unit Tested with Pytest

## Tech Stack

- **Backend:** FastAPI, Python 3.11
- **Database:** PostgreSQL, SQLAlchemy
- **Authentication:** JWT, OAuth2
- **Server:** Uvicorn
- **Deployment:** Render
- **Containerization:** Docker

## Project Structure
├── main.py              # FastAPI application entry point
├── database.py          # Database connection and session
├── model.py             # SQLAlchemy models
├── schemas.py           # Pydantic schemas for validation
├── crud.py              # CRUD operations
├── auth.py              # Authentication routes
├── security.py          # JWT token and password hashing
├── requirements.txt     # Project dependencies
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker compose for DB
├── employee.db          # Local SQLite DB
└── tests/               # Test casesjavascript
## API Endpoints

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| POST | `/register` | Register a new user | No |
| POST | `/login` | Login and get access token | No |
| GET | `/employees` | Get all employees | Yes |
| POST | `/employees` | Create a new employee | Yes |
| GET | `/employees/{id}` | Get employee by ID | Yes |
| PUT | `/employees/{id}` | Update employee details | Yes |
| DELETE | `/employees/{id}` | Delete employee | Yes |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Employee_-API.git
cd Employee_-API2. Create virtual environmentbashpython -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate3. Install dependenciesbashpip install -r requirements.txt4. Environment Variables
Create a .env file in root:javascriptDATABASE_URL=postgresql://username:password@localhost/employee_db
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=305. Run the applicationbashuvicorn main:app --reloadAPI will be available at: http://localhost:8000
Docs at: http://localhost:8000/docs
Docker Setupbashdocker-compose up --buildDeployment
This project is deployed on Render with PostgreSQL.
Live URL: employee-api-93no.onrender.com
Author
Darshan
Python Developer | FastAPI Enthusiast