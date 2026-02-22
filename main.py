from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_FILE_PATH = "q-fastapi.csv"  # change if needed


@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(None, alias="class")):
    students = []

    try:
        with open(CSV_FILE_PATH, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "studentId": int(row["studentId"]),
                    "class": row["class"]
                }

                if class_:
                    if student["class"] in class_:
                        students.append(student)
                else:
                    students.append(student)

    except Exception as e:
        return {"error": str(e)}

    return {"students": students}