from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cargoes")
def get_cargoes():

    with open("data/cargoes.json") as f:
        return json.load(f)


@app.get("/vessels")
def get_vessels():

    with open("data/vessels.json") as f:
        return json.load(f)