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
## 🌐 Local URLs

| Component | URL |
|---|---|
| Frontend | http://localhost:5173 |
| API Gateway | http://127.0.0.1:8000 |
| Gateway Documentation | http://127.0.0.1:8000/docs |
| Authentication Service | http://127.0.0.1:8001 |
| Authentication Documentation | http://127.0.0.1:8001/docs |
| Student Service | http://127.0.0.1:8002 |
| Student Documentation | http://127.0.0.1:8002/docs |
| Course Service | http://127.0.0.1:8003 |
| Course Documentation | http://127.0.0.1:8003/docs |

*These URLs will work after the corresponding services are implemented and running locally.*

## 🚀 Running the Project

Open separate PowerShell terminals in the project root. Run each service from its own directory after completing its implementation and installing its dependencies.

### API Gateway

```powershell
cd api-gateway
python -m uvicorn main:app --reload --port 8000
```

### Authentication Service

```powershell
cd auth-service/app
python -m uvicorn main:app --reload --port 8001
```

### Student Service

```powershell
cd student-service/app
python -m uvicorn main:app --reload --port 8002
```

### Course Service

```powershell
cd course-service/app
python -m uvicorn main:app --reload --port 8003
```

### Frontend

After creating the React application:

```powershell
cd frontend
npm install
npm run dev
```

## 📦 Project Resources

- **Source Code:** Available in this repository.
- **Postman Collection:** `postman/`
- **Screenshots:** `screenshots/`

## 📊 Project Status

The repository structure and documentation are being prepared. The services and frontend must be implemented before the application can run.

## 👨‍💻 Author

**Bharath Reddy**

## 📈 Project Status

**Status:** Initial project structure created. Development and testing are pending.

## 👨‍💻 Author

**Bharath Reddy**
