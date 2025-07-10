
# 🚀 Insurance Premium Category Predictor (FastAPI + ML + Streamlit)

An intelligent full-stack web app powered by **FastAPI**, **Pydantic**, and **Machine Learning** to predict **insurance premium category** based on user profile. Built with modern web standards, smart validations, and an intuitive Streamlit frontend.  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-API-green) ![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-orange) ![ML](https://img.shields.io/badge/ML-Model-success)

---

## 🎯 Use Case

This project predicts the **insurance premium category** using user demographic & lifestyle inputs like:
- Age, BMI, Occupation, Smoking habits
- Income, City, etc.

---

## 💡 Features

- ✅ FastAPI backend with RESTful API for predictions  
- ✅ Real-time prediction using a trained ML model  
- ✅ Smart input validation with **Pydantic**
- ✅ Auto-calculated features: **BMI**, **Lifestyle Risk**, **City Tier**
- ✅ Frontend built with **Streamlit**  
- ✅ Clean UI/UX to interact with backend model  
- ✅ OpenAPI Docs at `/docs` (Swagger)

---

## 📺 Live Demo Preview

> _(Add your screenshots here later)_  
> ![Preview](https://via.placeholder.com/1000x300.png?text=Insurance+Prediction+UI)

---

## 🛠 Tech Stack

- **Backend**: FastAPI + Pydantic
- **Model**: Trained sklearn model (`model_f.pkl`)
- **Frontend**: Streamlit
- **Deployment**: Uvicorn

---

## 📦 File Structure

```
📁 InsurancePredictor/
├── app.py                 # FastAPI backend
├── frontend.py            # Streamlit frontend
├── model_f.pkl            # Trained ML model
├── fastapi_ml_model.ipynb # Training notebook
└── README.md
```

---

## ⚙️ How It Works

### 🧠 ML Model Input Features:
- `bmi` (calculated from height & weight)
- `age_group` (young, adult, middle_aged, senior)
- `lifestyle_risk` (low, medium, high)
- `city_tier` (1, 2, 3)
- `income_lpa` (float)
- `occupation` (encoded)

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourname/insurance-predictor.git
cd insurance-predictor
```

### 2️⃣ Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI server
```bash
uvicorn app:app --reload
```

### 4️⃣ Run the Streamlit frontend
```bash
streamlit run frontend.py
```

---

## 🔥 API Documentation

Once FastAPI is running, navigate to:

- 📘 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 🔎 Root Endpoint: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Sample JSON Input

```json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 12.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

---

## 💻 Prediction Output

```json
{
  "predicted_category": "Gold"
}
```

---

## 👨‍💻 Author

Developed with ❤️ by [**Pratham Suthar**](https://github.com/pratham14-coder)  
For any queries, reach out via GitHub.

---

## 📥 Download Project

[Click here to download ZIP](https://github.com/pratham14-coder/insurance-predictor/archive/refs/heads/main.zip)

---

## 🪪 License

This project is open-source under the [MIT License](LICENSE).

> _Empower Insurance Tech with AI 🚀_
