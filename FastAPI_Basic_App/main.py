# Import the FastAPI class from the fastapi package
from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Define a GET endpoint at the root URL ("/")
@app.get("/")
def hello():
    # Return a JSON response with a welcome message
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    # Return a JSON response with an about message
    return {"message": "This is a simple FastAPI application."} 

@app.get('/services')
def services():
    # Return a JSON response with a services message
    return {"message": "We offer various services including web development, data analysis, and more."}