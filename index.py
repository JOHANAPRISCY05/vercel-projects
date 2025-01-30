from fastapi import FastAPI
from typing import List
import json

app = FastAPI()

with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

async def get_marks(name: List[str]):
     marks = [data.get(n, None) for n in name]

     return{"marks": marks}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
