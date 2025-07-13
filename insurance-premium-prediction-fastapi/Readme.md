
# 🧠 Insurance Premium Prediction API 🚀

A production-ready FastAPI app that predicts **insurance premiums** using a trained machine learning model.  
Built for performance, scalability, and clarity.

---

## 📌 Key Features

- 🚀 FastAPI backend for real-time predictions
- 🧠 ML model integration (salary, health, and lifestyle-based)
- 🔐 Input validation via Pydantic
- 🗃️ Modular structure: easy to maintain and extend
- 📊 Interactive API docs (Swagger & Redoc)

---

## 📁 Folder Structure

```
insurance-premium-prediction-fastapi/
│
├── app.py                   # Main FastAPI application
├── model/                   # ML model and logic
├── schema/                  # Request and response models
├── config/                  # Configuration settings
├── requirements.txt         # Project dependencies
├── .vscode/                 # (Optional) Editor settings
└── README.md                # Project documentation
```

---

## 🎯 Sample Input (JSON)

```json
{
  "age": 30,
  "weight": 72.5,
  "height": 1.75,
  "income_lpa": 12,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

## ✅ Sample Output

```json
{
  "predicted_premium": 7321.84,
  "message": "Prediction successful"
}
```

---

## 🧪 Run the API Locally

```bash
# Clone the repo and move into the directory
git clone <repo-url>
cd insurance-premium-prediction-fastapi

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI app
uvicorn app:app --reload
```

📍 Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI

---

## 📚 API Docs

- [✔️ Swagger UI](http://127.0.0.1:8000/docs)
- [📘 Redoc](http://127.0.0.1:8000/redoc)

---

## 👨‍💻 Author

**Your Name**  
🔗 [GitHub](https://github.com/pratham14-coder/FastAPI/tree/main/insurance-premium-prediction-fastapi)  
📬 Connect on [LinkedIn](https://linkedin.com/prathamsuthar)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Use it freely and contribute back with improvements!

---
