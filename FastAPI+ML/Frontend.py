import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")

st.title("💡 Insurance Premium Category Predictor")
st.markdown("Please fill in the details to get a prediction.")

# Input form
age = st.number_input("🧓 Age", min_value=1, max_value=119, value=30)
weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("📏 Height (meters)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("💰 Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("🚬 Are you a smoker?", options=[True, False])
city = st.text_input("🏙️ City", value="Mumbai")
occupation = st.selectbox("💼 Occupation", [
    'retired', 'freelancer', 'student', 'government_job',
    'business_owner', 'unemployed', 'private_job'
])

# Prediction button
if st.button("🔍 Predict Premium Category"):
    # Prepare data
    data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        # Send request to FastAPI
        response = requests.post(API_URL, json=data)

        # Check response
        if response.status_code == 200:
            result = response.json()

            # Display prediction result
            st.success(f"✅ Predicted Premium Category: **{result['predicted_category']}**")

            # Optional: show confidence and probabilities if backend sends them
            if 'confidence' in result:
                st.write("📈 Model Confidence:", result['confidence'])

            if 'class_probabilities' in result:
                st.subheader("🔢 Class Probabilities")
                st.json(result['class_probabilities'])

        else:
            st.error(f"❌ API returned status code: {response.status_code}")
            st.text(response.text)

    except requests.exceptions.ConnectionError:
        st.error("⚠️ Could not connect to FastAPI server. Make sure it's running at http://localhost:8000.")

