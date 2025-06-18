# Import the FastAPI class to create the web API
from fastapi import FastAPI

# Import json module to work with JSON files
import json

# Create an instance of the FastAPI application
app = FastAPI()

# Function to load patient data from a JSON file
def data_load():
    # Open the file 'patients.json' in read mode
    with open('patients.json', 'r') as f:
        # Load the JSON data into a Python dictionary or list
        data = json.load(f)
    
    # Return the loaded data
    return data

# Root route of the API
@app.get("/")
def hello():
    # Returns a welcome message for the Patient Management System
    return {'message': 'Patient Management System'}

# About route of the API
@app.get('/about')
def about():
    # Returns information about the project
    return {'message': 'A fully functional Project API to manage Hospital Patient Records'}

# View route to display all patient data
@app.get('/view')
def view():
    # Call the data_load function to get patient data from the file
    data = data_load()

    # Return the patient data as a response
    return data
