import requests
from fastapi import FastAPI

app = FastAPI()
url = 'https://raw.githubusercontent.com/Laboratoria/BOG001-data-lovers/master/src/data/rickandmorty/rickandmorty.json'
response = requests.get(url)
data = response.json()

@app.get("/personajes")
def obtener_personaje():
    return data['results']

@app.put("/personajes/{nombre}")
def matar_personaje(nombre: str, estado: str):
    for personaje in data['results']:
            if personaje['name'].lower() == nombre.lower():
                personaje['status'] = estado

     

