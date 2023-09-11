from fastapi import FastAPI

app = FastAPI()


@app.get("/students")
async def get_students():
    return { "students": [{ "name": "john", "age": 25  }, { "name": "jane", "age": 40 }] }


@app.post("/students")
async def add_student(student):
    return { "ok": True, "id": 12 }


@app.get("/students/{id}")
async def get_student(id: int):
    return { "name": "john", "age": 25 }


@app.patch("/students/{id}")
async def update_student(id: int):
    return { "name": "john", "age": 25 }


@app.delete("/students/{id}")
async def remove_student(id: int):
    return { "ok": True }
