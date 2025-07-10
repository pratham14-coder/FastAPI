# 🩺 Patient Health Management System using FastAPI

An intelligent health record management system built with **FastAPI** that stores patient data, calculates **BMI** & health verdicts, and supports full **CRUD operations** with clean API documentation.

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/fastapi-0.110.0-green)

---

## 📸 Project Preview

> _Smart BMI-based health dashboard via REST API_  

![Preview](https://via.placeholder.com/1000x300.png?text=Patient+Management+API+with+FastAPI)

---

## 🚀 Features

✅ Create new patients with validation  
✅ Automatically calculate **BMI** and **health status**  
✅ Get all patient records or filter by ID  
✅ Update or delete patient details  
✅ Sort records by height, weight, or BMI  
✅ Data stored locally in `patients.json`  
✅ OpenAPI docs at `/docs`

---

## 🛠️ Technologies Used

- ⚡ FastAPI
- 🔍 Pydantic
- 📁 JSON for storage
- 🔄 Uvicorn (ASGI server)
- 🧪 Swagger UI

---

## 📦 API Endpoints

| Method | Endpoint            | Description                    |
|--------|---------------------|--------------------------------|
| GET    | `/`                 | Welcome message                |
| GET    | `/view`             | View all patients              |
| GET    | `/patient/{id}`     | View patient by ID             |
| GET    | `/sort?sort_by=bmi`| Sort by BMI/height/weight      |
| POST   | `/create`           | Create a new patient           |
| PUT    | `/edit?patient_id=` | Update patient by ID           |
| DELETE | `/delete/{id}`      | Delete patient                 |

🔗 **Swagger API Docs**: [`/docs`](http://127.0.0.1:8000/docs)

---

## 📂 Project Structure

```
📁 FastAPI_Patient_App/
│
├── main.py            # Main FastAPI app
├── patients.json      # Local database (JSON)
└── README.md
```

---

## 💻 Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/pratham14-coder/FastAPI.git
cd FastAPI
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 4️⃣ Run the FastAPI server

```bash
uvicorn main:app --reload
```

Open in browser:
- Home: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📝 Sample JSON

```json
{
  "P001": {
    "name": "John Doe",
    "city": "Mumbai",
    "age": 32,
    "gender": "male",
    "height": 1.75,
    "weight": 75,
    "bmi": 24.49,
    "verdict": "Normal"
  }
}
```

---

## 📬 Contact & Contribution

Feel free to fork the repo, raise issues, or contribute!  
Created by [**Pratham Suthar**](https://github.com/pratham14-coder)

---

## ⬇️ Download This Project

> Click below to download the full project ZIP  
[**🔽 Download Project**](https://github.com/pratham14-coder/FastAPI/archive/refs/heads/main.zip)

---

## 🏁 License

This project is licensed under the **MIT License**. Feel free to use and modify.

---

> _Built with 💚 using FastAPI to help manage patient health easily._
