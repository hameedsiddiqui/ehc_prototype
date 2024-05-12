from fastapi import FastAPI, HTTPException, Depends, Security, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import mysql.connector

app = FastAPI()

security = HTTPBasic()

# Function to establish a connection to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin",
        database="ehc_prototype"  # Assuming this is the name of your database
    )

# Function to execute SQL queries
def execute_query(query, values=None):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
        else:
            result = cursor.lastrowid
        connection.commit()
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        raise
    finally:
        cursor.close()
        connection.close()

# Add record to Owner table
@app.get("/add_Owner")
def add_owner(credentials: HTTPBasicCredentials = Depends(security), name: str, contact_information: str):
    if not (credentials.username == "admin" and credentials.password == "admin"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    query = "INSERT INTO Owner (name, contact_information) VALUES (%s, %s)"
    values = (name, contact_information)
    owner_id = execute_query(query, values)
    return {"owner_id": owner_id}

# Add record to Model table
@app.get("/add_Model")
def add_model(credentials: HTTPBasicCredentials = Depends(security), description: str, application_areas: str, params: str, metrics: str, confidence: str, owner_id: int, last_update_timestamp: str):
    if not (credentials.username == "admin" and credentials.password == "admin"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    query = "INSERT INTO Model (description, application_areas, params, metrics, confidence, owner_id, last_update_timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (description, application_areas, params, metrics, confidence, owner_id, last_update_timestamp)
    model_id = execute_query(query, values)
    return {"model_id": model_id}

# Add record to Dataset table
@app.get("/add_Dataset")
def add_dataset(credentials: HTTPBasicCredentials = Depends(security), description: str, format: str, size: float):
    if not (credentials.username == "admin" and credentials.password == "admin"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    query = "INSERT INTO Dataset (description, format, size) VALUES (%s, %s, %s)"
    values = (description, format, size)
    dataset_id = execute_query(query, values)
    return {"dataset_id": dataset_id}

# Add record to Metric table
@app.get("/add_Metric")
def add_metric(credentials: HTTPBasicCredentials = Depends(security), name: str, value: float):
    if not (credentials.username == "admin" and credentials.password == "admin"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    query = "INSERT INTO Metric (name, value) VALUES (%s, %s)"
    values = (name, value)
    metric_id = execute_query(query, values)
    return {"metric_id": metric_id}

# Add record to ModelDataset table
@app.get("/add_ModelDataset")
def add_model_dataset(credentials: HTTPBasicCredentials = Depends(security), model_id: int, dataset_id: int):
    if not (credentials.username == "admin" and credentials.password == "admin"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    query = "INSERT INTO ModelDataset (model_id, dataset_id) VALUES (%s, %s)"
    values = (model_id, dataset_id)
    execute_query(query, values)
    return {"message": "Record added successfully"}

# Add record to ModelMetric table
@app.get("/add_ModelMetric")
def add_model_metric(credentials: HTTPBasicCredentials = Depends(security), model_id: int, metric_id: int):
    if not (credentials.username == "admin" and credentials.password == "admin"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    query = "INSERT INTO ModelMetric (model_id, metric_id) VALUES (%s, %s)"
    values = (model_id, metric_id)
    execute_query(query, values)
    return {"message": "Record added successfully"}

# Get records from any table
@app.get("/get_{table_name}")
def get_records(table_name: str, id: int = None, credentials: HTTPBasicCredentials = Depends(security)):
    if not (credentials.username == "admin" and credentials.password == "admin"):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    if id:
        query = f"SELECT * FROM {table_name} WHERE id = %s"
        values = (id,)
    else:
        query = f"SELECT * FROM {table_name}"
        values = None
    records = execute_query(query, values)
    if not records:
        raise HTTPException(
            status_code=404,
            detail=f"No records found in table {table_name}"
        )
    return records

