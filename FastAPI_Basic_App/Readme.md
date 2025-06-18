
# 🚀 FastAPI Basic Application

A modern, high-performance API built with **FastAPI** — a blazing-fast Python web framework for building web APIs. This is a starter project demonstrating basic route handling and JSON response capabilities.

---

## 📌 Features

- ✅ FastAPI with auto-generated docs (`Swagger UI` & `ReDoc`)
- ✅ Clean and simple GET endpoint
- ✅ JSON response structure
- ✅ Easy to expand for real-world use

---

## 🔧 Tech Stack

- **Language**: Python 3.7+
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Server**: Uvicorn (recommended for running)

---

## 📂 Project Structure

```
.
├── main.py          # FastAPI application with routes
└── README.md        # Project documentation
```

---

## 🚀 How to Run This FastAPI App

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fastapi-basic-app.git
cd fastapi-basic-app
```

### 2. Create and activate a virtual environment (recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn
```

### 4. Start the FastAPI server
```bash
uvicorn main:app --reload
```

The `--reload` flag enables hot-reloading, so changes are auto-reflected during development.

---

### 🔍 Access the API

- Root Endpoint: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc Docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🙌 Contributing

Feel free to fork this repo and open a PR if you'd like to add something cool. All improvements are welcome!

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
