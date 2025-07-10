from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse
from typing import Annotated, Literal, Optional
import json

app = FastAPI()


class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[
        Literal["male", "female", "others"],
        Field(..., description="Gender of the patient"),
    ]
    height: Annotated[
        float, Field(..., gt=0, description="Height of the patient in mtrs")
    ]
    weight: Annotated[
        float, Field(..., gt=0, description="Weight of the patient in kgs")
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"


def data_load():
    with open("patients.json", "r") as f:
        data = json.load(f)  # Load JSON data and convert it into Python dictionary
        return data


def save_data(data):
    with open("patient.json", "w") as f:
        json.dump(data, f)


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal["male", "female"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


@app.get("/")
def hello():
    return {"message": "Hello Coders"}  # Simple response message


@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}


@app.get("/view")
def view():
    data = data_load()  # Load data from file
    return data  # Return all patient data


@app.get("/patient/{patient_id}")
def view_patients(patient_id: str):
    data = data_load()
    if patient_id in data:
        return data[patient_id]  # Return patient info if ID found
    return {"error": "patient not found"}  # Return error message if ID not found


@app.get("/patients/{patient_id}")
def view_patients(
    patient_id: str = Path(..., description="ID of the patients in DB", example="P001")
):
    data = data_load()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not Found in DB")


#
@app.get("/sort")
def sort_patient(
    sort_by: str = Query(
        ..., description="Sort the patient data by height, weight, or BMI"
    ),
    order: str = Query(
        "asc", description="Sort in ascending (asc) or descending (desc) order"
    ),
):

    valid_feild = ["height", "weight", "bmi"]

    if sort_by not in valid_feild:
        raise HTTPException(
            status_code=400, detail=f"Invalid field selected. Choose from {valid_feild}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400, detail='Invalid order selected. Choose "asc" or "desc"'
        )

    data = data_load()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order
    )

    return sorted_data


@app.post("/create")
def create_patient(patient: Patient):
    # load data of patient
    data = data_load()

    # Check if the patient is already exits in database or not
    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail=f"{patient.id} is already exit in database so create a different patientid",
        )

    # Add the new patient to the data
    data[patient.id] = patient.model_dump(exclude=["id"])

    # save  into json from
    save_data(data)

    return JSONResponse(
        status_code=201, content={"message": "patient created successfully"}
    )


# edit the Existing patient data


@app.put("/edit")
def edit_patient_info(patient_id: str, patient_update: PatientUpdate):
    # Load the patient data
    data = data_load()
    # Check if patient id is exit or not
    if patient_id not in data:
        raise HTTPException(
            status_code=400,
            detail={f"{patient_id} is already not exist in patient data?Try again"},
        )

    existing_patient_info = data[patient_id]
    # pyd -> dict
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info["id"] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)


    # -> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude="id")

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    
    return JSONResponse(status_code=200, content={'message':'patient updated'})



@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = data_load()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})
