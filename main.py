
from AI import Generate
from pydantic import BaseModel

# print(Generate("what is the sum of 100 + 100"))

class Promptschema(BaseModel):
    Prompt: str

from fastapi import FastAPI , Body
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.get("/")
def DefaultRoute():
    return "Welcome to AI"

@app.post("/api/AccessAI/")
def Gen(data: Promptschema = Body(...)):
    RES =Generate(data.Prompt)
    print(f"Successful!!!")
    return RES