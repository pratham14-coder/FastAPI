# ✅ Import necessary modules from FastAPI and Python
from fastapi import FastAPI, Path, HTTPException, Query
import json 

# ✅ Create a FastAPI app instance
app = FastAPI()

# 🔄 Function to load patient data from a JSON file
def data_load():
    with open("patients.json", "r") as f:
        data = json.load(f)  # Load JSON data and convert it into Python dictionary
        return data

# 🏠 Root endpoint ("/") that returns a welcome message
@app.get("/")
def hello():
    return {"message": "Hello Coders"}  # Simple response message

# ℹ️ About endpoint returns information about the API
@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}

# 👁️ View all patients in the database
@app.get("/view")
def view():
    data = data_load()  # Load data from file
    return data         # Return all patient data

# 🔍 Get specific patient by ID (basic version without error handling)
@app.get('/patient/{patient_id}')
def view_patients(patient_id: str):
    data = data_load()
    if patient_id in data:
        return data[patient_id]  # Return patient info if ID found
    return {"error": "patient not found"}  # Return error message if ID not found

# 🔍 Get specific patient by ID (better version with Path and proper error)
@app.get('/patients/{patient_id}')
def view_patients(
    patient_id: str = Path(..., description='ID of the patients in DB', example='P001')
):
    data = data_load()
    if patient_id in data:
        return data[patient_id]  # Return the matching patient data
    # If patient ID not found, raise proper HTTP error with status code 404
    raise HTTPException(status_code=404, detail="Patient not Found in DB")

# 🔃 Sort patient data by height, weight, or BMI
@app.get("/sort")
def sort_patient(
    sort_by: str = Query(..., description="Sort the patient data by height, weight, or BMI"),
    order: str = Query("asc", description="Sort in ascending (asc) or descending (desc) order")
):
    # ✅ Valid fields that can be used for sorting
    valid_feild = ["height", "weight", "bmi"]

    # ❌ If sort_by is not valid, raise an HTTP 400 error
    if sort_by not in valid_feild:
        raise HTTPException(status_code=400, detail=f'Invalid field selected. Choose from {valid_feild}')
    
    # ❌ If order is invalid, raise an HTTP 400 error
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order selected. Choose "asc" or "desc"')
    
    # 🔄 Load patient data
    data = data_load()

    # 🔁 Determine sort order: True for descending, False for ascending
    sort_order = True if order == 'desc' else False

    # 📊 Sort the patient dictionaries based on the selected field
    # If a patient doesn't have the field, treat its value as 0
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data  # ✅ Return sorted data
