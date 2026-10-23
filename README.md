# Student Management System – Microservices

A Student Management System designed using a microservices architecture to organize student records, manage courses, and handle student enrollment.

## 📌 Project Overview

This project is organized into independent services for authentication, student management, course management, and API routing. A frontend directory is included for the user interface.

## 🛠️ Technology Stack

- **Backend:** Python, FastAPI
- **Frontend:** React, Vite
- **Database:** SQLite
- **Authentication:** JWT (JSON Web Tokens)
- **API Communication:** REST APIs
- **API Testing:** Postman
- **HTTP Server:** Uvicorn

## 📂 Project Structure

```text
student-management-system-microservices/
│
├── api-gateway/
│   └── main.py
│
├── auth-service/
│   └── app/
│       └── main.py
│
├── student-service/
│   └── app/
│       └── main.py
│
├── course-service/
│   └── app/
│       └── main.py
│
├── frontend/
│
├── postman/
│
├── screenshots/
│
├── .gitignore
└── README.md
```

## ✨ Planned Features

- User registration and login
- JWT-based authentication
- Add, view, update, and delete student records
- Create and manage courses
- Enroll students in courses
- View students enrolled in each course
- Centralized API access through an API Gateway
- API testing using Postman

## ⚙️ Service Configuration

| Service | Port |
|---|---:|
| API Gateway | 8000 |
| Authentication Service | 8001 |
| Student Service | 8002 |
| Course Service | 8003 |
| Frontend | 5173 |

*These are planned port assignments; update them if your implementation uses different ports.*

## 📸 Screenshots

Application screenshots will be added here as development progresses.

Suggested screenshots:

- Login page
- Student dashboard
- Add student form
- Course management page
- Enrolled students page

## 🧪 API Testing

Postman collections and API test examples will be maintained in the `postman/` directory.

## 🚀 Getting Started

The project structure is being prepared. Setup instructions, dependencies, environment variables, database configuration, and service startup commands will be documented after implementation.

## 📈 Project Status

**Status:** Initial project structure created. Development and testing are pending.

## 👨‍💻 Author

**Bharath Reddy**
