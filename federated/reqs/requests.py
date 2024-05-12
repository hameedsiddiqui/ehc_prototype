import requests

# Base URL of your FastAPI server
base_url = "http://localhost:8000"

# Endpoint for adding an owner
add_owner_endpoint = f"{base_url}/add_Owner"

# Endpoint for adding a model
add_model_endpoint = f"{base_url}/add_Model"

# Function to add an owner
def add_owner(name, contact_information):
    response = requests.get(add_owner_endpoint, params={"name": name, "contact_information": contact_information})
    if response.status_code == 200:
        print("Owner added successfully")
    else:
        print("Failed to add owner")

# Function to add a model
def add_model(description, application_areas, params, metrics, confidence, owner_id, last_update_timestamp):
    response = requests.get(add_model_endpoint, params={"description": description, "application_areas": application_areas, "params": params, "metrics": metrics, "confidence": confidence, "owner_id": owner_id, "last_update_timestamp": last_update_timestamp})
    if response.status_code == 200:
        print("Model added successfully")
    else:
        print("Failed to add model")


