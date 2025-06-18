
# 🏥 Patient Management API - Powered by FastAPI

A modern and blazing-fast RESTful API built with **FastAPI** to manage hospital patient records. This basic project demonstrates how to serve structured JSON data, organize endpoints, and build scalable backend services.

---

## ✨ Features

- 🔥 Built with FastAPI (asynchronous & high performance)
- 📁 Reads data from a local `patients.json` file
- 📊 RESTful endpoints for viewing and describing the patient system
- 📄 Auto-generated Swagger UI & ReDoc API documentation
- 🚀 Ready for integration and deployment

---

## 🛠️ Tech Stack

- **Language**: Python 3.7+
- **Framework**: FastAPI
- **Server**: Uvicorn (ASGI)

---

## 📁 Project Structure

```
📦 patient-management-api
├── 📄 main.py             # Main FastAPI application
├── 📄 patients.json       # JSON file containing patient data
└── 📄 README.md           # Project documentation
```

---

## 🚀 How to Run This API

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/patient-management-api.git
cd patient-management-api
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install fastapi uvicorn
```

### 4️⃣ Run the API Server
```bash
uvicorn main:app --reload
```

✅ Access the API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Welcome message for Patient Management System |
| GET    | `/about` | Describes the project purpose and functionality |
| GET    | `/view`  | Returns all patient records from `patients.json` |

---

## 🔍 API Docs

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧠 Code Explanation

```python
# Import the FastAPI class to create the web API
from fastapi import FastAPI

# Import json module to work with JSON files
import json

# Create an instance of the FastAPI application
app = FastAPI()

# Function to load patient data from a JSON file
def data_load():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

# Root route of the API
@app.get("/")
def hello():
    return {'message': 'Patient Management System'}

# About route of the API
@app.get('/about')
def about():
    return {'message': 'A fully functional Project API to manage Hospital Patient Records'}

# View route to display all patient data
@app.get('/view')
def view():
    data = data_load()
    return data
```

---

## 🧾 Breakdown

- **FastAPI Setup**: Initializes the web app.
- **JSON Data Loading**: Reads and parses `patients.json`.
- **Three Routes**:
  - `/` for welcome message
  - `/about` for project info
  - `/view` for returning all patients’ data as JSON

---

## 🙌 Contributing

Contributions are welcome! Feel free to fork, enhance, or expand the API.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Tip

Add POST/PUT/DELETE methods, validation using Pydantic models, and connect a database for full CRUD capability.
