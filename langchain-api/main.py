from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    message: str

@app.post("/generate")
def generate(prompt: Prompt):

    return {"response": f"AI says: You said '{prompt.message}'"}
