
# 🚀 FastAPI Basic Application

A modern, high-performance web API built with **FastAPI** — a lightning-fast Python framework for building robust backend services with automatic interactive docs.

---

## ✨ Features

- ⚡ Ultra-fast performance with FastAPI
- 📄 Auto-generated, interactive API documentation (Swagger UI & ReDoc)
- 🧼 Clean and minimal endpoint design
- 🧩 Easily extensible for real-world projects

---

## 🛠️ Tech Stack

- **Language**: Python 3.7+
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/) with hot-reload

---

## 📁 Project Structure

```
📦 fastapi-basic-app
├── 📄 main.py        # Core FastAPI application
└── 📄 README.md      # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-basic-app.git
cd fastapi-basic-app
```

### 🧪 2. Set Up a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 🟢 4. Run the Development Server

```bash
uvicorn main:app --reload
```

✅ The app will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 API Access

| Method | Endpoint | Description            |
|--------|----------|------------------------|
| GET    | `/`      | Returns welcome message |

### 🔍 Auto Docs

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc UI](http://127.0.0.1:8000/redoc)

---

## 🧠 Code Walkthrough

```python
# Import the FastAPI class from the fastapi package
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Define a GET endpoint at the root URL ("/")
@app.get("/")
def hello():
    # Return a JSON response with a welcome message
    return {"message": "Hello, World!"}
```

### 🔎 Explanation

- **Import FastAPI**: Loads the web framework into your script.
- **Create App Instance**: Initializes the API app using `FastAPI()`.
- **Define Endpoint**: The `@app.get("/")` decorator maps the root URL to the `hello` function.
- **Return JSON**: FastAPI automatically converts dictionaries into JSON responses.

---

## 🤝 Contributing

We welcome all contributions! Feel free to fork this repo and submit a pull request to improve or extend the application.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

💡 **Pro Tip**: Explore more FastAPI features like request validation, path/query parameters, dependency injection, and middleware to build full-stack, production-ready APIs.
