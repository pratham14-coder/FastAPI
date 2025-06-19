
# 🚀 FastAPI3 - Patient Management API

A blazing-fast, modern RESTful API built with **FastAPI** to manage hospital patient records using a JSON-based datastore. Ideal for demoing API design, sorting, error handling, and dynamic querying.

---

## 🧩 Tech Stack

- ⚡ **FastAPI** — High-performance web framework
- 🐍 **Python 3.10+**
- 🔗 **Uvicorn** — Lightning-fast ASGI server
- 📂 **JSON** — For lightweight, file-based patient storage

---

## 📦 Features

✅ View all patients  
✅ Retrieve patient by ID (basic + validated)  
✅ Sort patients by height, weight, or BMI  
✅ Clean error handling for invalid inputs  
✅ Interactive Swagger and ReDoc documentation  

---

## 🛠️ Setup Instructions

### 🔁 Clone Repository

```bash
git clone https://github.com/pratham14-coder/FastAPI.git
cd FastAPI/FastAPI3
```

### 🐍 Create Virtual Environment

```bash
python -m venv myenv
# For Git Bash
source myenv/Scripts/activate
# For PowerShell
myenv\Scripts\Activate.ps1
```

### 📥 Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

📍 Access Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
📍 Access ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📁 Project Structure

```
FastAPI3/
│
├── main.py             # 🌐 FastAPI application
├── patients.json       # 🩺 Patient data in JSON format
├── README.md           # 📘 Project documentation
├── .gitignore          # 🚫 Ignore virtual environments
└── myenv/              # 🐍 Python virtual environment (not pushed)
```

---

## 🌐 API Endpoints Overview

| Method | Endpoint                  | Description                           |
|--------|---------------------------|---------------------------------------|
| GET    | `/`                       | Welcome message                       |
| GET    | `/about`                  | About the API                         |
| GET    | `/view`                   | View all patients                     |
| GET    | `/patient/{patient_id}`   | Basic patient ID fetch                |
| GET    | `/patients/{patient_id}`  | Validated patient ID fetch            |
| GET    | `/sort`                   | Sort patients by height/weight/BMI    |

### 🔄 Sorting Example

```http
GET /sort?sort_by=bmi&order=desc
```

🔑 Fields: `height`, `weight`, `bmi`  
📊 Orders: `asc`, `desc`

---

## 🛡️ .gitignore Recommendation

```gitignore
myenv/
*.pyc
__pycache__/
.env
```

---

## 📌 Sample JSON Format

```json
{
  "P001": {"name": "John", "height": 170, "weight": 65, "bmi": 22.5},
  "P002": {"name": "Alice", "height": 160, "weight": 70, "bmi": 27.3}
}
```

---

## 👨‍💻 Author

**Pratham Suthar** — [GitHub](https://github.com/pratham14-coder)  
Made with ❤️ using FastAPI

---

## 📜 License

This project is open-source and free to use under the MIT License.
