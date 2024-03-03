import requests
from bs4 import BeautifulSoup


def get_pokemon_name(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_name = pokemon_data["name"]
        return pokemon_name
    else:
        return None


def get_pokemon_name_by_scraping(pokemon_id):
    url = "https://pokemon.gameinfo.io/es"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    pokemon_list = soup.find("div", class_="pokemon-list").find_all("div", class_="gen")
    pokemon_name = None

    for pokemon in pokemon_list:
        id = pokemon.find("div", class_="id").text.strip()
        if id == pokemon_id:
            pokemon_name = pokemon.find("h2").text.strip().lower()
    return pokemon_name

def pokemon_coordenadas():

    url = "https://coordsgo.com/pkm90"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    pokemon_list = soup.find_all("div", class_="pkm")
    names = []
    shinies = []

    for pokemon in pokemon_list:
        info_div = pokemon.find("div", class_="info")
        name_div = info_div.find("div", class_="name")
        shiny = name_div.find("div", class_="shiny").text.strip()
        name = name_div.find("div", attrs={"data-v-6e6ad457": ""}).text.strip()
        names.append(name)
        shinies.append(shiny)

    print(shinies)
    print(names)



