
# Basic E-Motorcycle API using FastAPI
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

# Message class defined in Pydantic
class Ebike(BaseModel):
    brand: str
    model: str
    trim: str
    range: float
    power: float # kiloWatts
    battery: float # kiloWatt hours



# Instantiate the FastAPI
app = FastAPI()

# In a real app, we would have a database.
# But, let's keep it super simple for now!
company_list = ["Sondor", "Zero"]
company_map = {}
for company in company_list:
    company_map[company] = []

@app.get("/status")
def get_status():
    """Get status of server."""
    return ({"status":  "running"})

@app.get("/companies", response_model=List[str])
def get_companies():
    """Get all companies in list form."""
    return company_list


@app.get("/companies/{company}", response_model=List[Ebike])
def get_bikes(company: str):
    """Get all bikes for the specified company."""
    return company_map.get(company)


@app.post("/add_bike", status_code=status.HTTP_201_CREATED)
def add_bike(bike: Ebike):
    """Post a new bike to the specified company."""
    company = bike.brand
    if company in company_list:
        company_map[company].append(bike)
        return bike
    else:
        company_map[company] = []
        company_map[company].append(bike)
        return bike
