from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
 
fakedb = []
class sampleModel(BaseModel):
    id:int
    name:str
    desc: Optional[str] = None


app = FastAPI()

@app.get("/")
def home():
    return {"greeting":"Hello World 2"}

@app.get("/addrow")
def add_row(row:sampleModel):
    fakedb.append(row.model_dump())
    print(fakedb)
    return fakedb[-1]

