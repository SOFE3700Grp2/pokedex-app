# main.py
import json
from fastapi import FastAPI, status, Response, Request
from collections import OrderedDict
from pydantic import BaseModel
from typing import Union, Optional
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"message": "Welcome to PokeDex"}

class PokemonO(BaseModel):
    id: int
    name: str
    type1: str
    type2: Optional[str] = None

file = open('./static/pokemon.json', "r")
data = json.loads(file.read())
pokemonL = data

@app.get("/pokemon/get/{pokemon_id}")
async def get_pokemon(pokemon_id: str, response: Response) -> PokemonO:
    try:
        result = pokemonL[pokemon_id]
    except KeyError:
        result = {"err":f"No such Pokemon: {pokemon_id}"}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return result

'''
{
    "id":1,
    "pokemon":"Bulbasaur",
    "type1":"Grass",
    "type2":"Poison"
}
'''