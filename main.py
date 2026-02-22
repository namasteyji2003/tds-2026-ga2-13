from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load CSV once
students = []

with open("q-fastapi.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(None, alias="class")):
    if class_:
        filtered = [s for s in students if s["class"] in class_]
        return {"students": filtered}
    return {"students": students}
