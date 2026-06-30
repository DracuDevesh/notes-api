# 📝 Notes API

A production-style REST API built with FastAPI following clean architecture principles.

This project demonstrates authentication, authorization, CRUD operations, testing, database migrations, and modern backend development practices.

---

## 🚀 Features

- User Registration
- User Login
- JWT Authentication
- OAuth2 Password Flow
- Protected Endpoints
- Notes CRUD
- User-specific Data Access
- Alembic Database Migrations
- Automated Tests with Pytest

---

## 🛠 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Alembic
- Pydantic
- Passlib (bcrypt)
- Python-JOSE (JWT)
- Pytest

---

## 📂 Project Structure

```text
app/
├── api/
├── core/
├── db/
├── dependencies/
├── models/
├── schemas/
├── services/
└── main.py

tests/

alembic/
```

---

## 🔐 Authentication

The API uses JWT Authentication.

Workflow:

```text
Register
     ↓
Login
     ↓
JWT Token
     ↓
Protected Endpoints
```

---

## 📌 API Endpoints

### Users

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /users/register | Register User |
| POST | /users/login | Login |
| GET | /users/me | Current User |

### Notes

| Method | Endpoint |
|---------|----------|
| POST | /notes |
| GET | /notes |
| GET | /notes/{id} |
| PUT | /notes/{id} |
| DELETE | /notes/{id} |

---

## 🧪 Running Tests

```bash
pytest
```

---

## ▶ Running Locally

```bash
git clone https://github.com/DracuDevesh/notes-api.git

cd notes-api

python -m venv .venv

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## 📈 Future Improvements

- Docker
- Docker Compose
- GitHub Actions
- Redis Caching
- Background Tasks
- Role-Based Access Control
- File Uploads

---

## 👨‍💻 Author

**Devesh Rai**