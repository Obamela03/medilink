MediLink Backend API

Backend service for the MediLink healthcare coordination platform.

Built with:

Django

Django REST Framework

SimpleJWT (JWT authentication)

SQLite (local development)

1. Requirements

Python 3.10+

pip

Git

2. Setup Instructions (Local Development)
2.1 Clone the Repository
git clone <your-repo-url>
cd medilink/backend
2.2 Create Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
2.3 Install Dependencies
pip install -r requirements.txt
2.4 Create .env File

Create a file named .env inside backend/:

DJANGO_SECRET_KEY=replace-me
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

CORS_ALLOWED_ORIGINS=http://localhost:3000

JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRY_MINUTES=15
REFRESH_TOKEN_EXPIRY_DAYS=7
2.5 Run Migrations
python manage.py makemigrations
python manage.py migrate
2.6 Start Development Server
python manage.py runserver

Server will run at:

http://127.0.0.1:8000/
3. API Base URL
http://127.0.0.1:8000/api
4. Authentication (JWT)

The API uses JSON Web Tokens.

Login

POST /api/auth/login/

Response:

{
  "refresh": "string",
  "access": "string"
}

Use the access token in requests:

Authorization: Bearer <access_token>
Refresh Token

POST /api/auth/refresh/

Request:

{
  "refresh": "token"
}
Current User

GET /api/auth/me/

Headers:

Authorization: Bearer <access_token>

Response:

{
  "id": 1,
  "username": "john",
  "email": "john@email.com",
  "role": "client"
}
5. User Registration

POST /api/auth/register/

Example:

{
  "username": "doctor1",
  "email": "doctor1@email.com",
  "password": "password123",
  "role": "doctor"
}

Roles available:

client

doctor

pharmacy

6. Available Endpoints (Week 1–2 Skeleton)
Doctors

GET /api/doctors/

Returns list of users with role = doctor.

Appointments (Stub)

GET /api/appointments/
POST /api/appointments/

Consultations (Stub)

GET /api/consultations/
POST /api/consultations/

Prescriptions (Stub)

GET /api/prescriptions/
POST /api/prescriptions/

Fulfill:
PATCH /api/prescriptions/{id}/fulfill/

7. Error Handling

Standard HTTP status codes:

200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

501 Not Implemented (for stubs)

Authentication error example:

{
  "detail": "Authentication credentials were not provided."
}
8. Notes for Frontend Team

All protected endpoints require:

Authorization: Bearer <access_token>

Register at least one user with role "doctor" to test /api/doctors/.

SQLite is used locally.

No business logic implemented yet for appointments, consultations, prescriptions (stubs only).

9. Assumptions (Current Phase)

Monolithic architecture

SQLite for development

No production deployment configuration yet

No PostgreSQL integration yet

No advanced permission enforcement yet

10. Project Status

Week 1 Complete:

Auth working

Role system working

API skeleton ready

Frontend integration can begin
