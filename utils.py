import requests

def get_pokemon_name(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_name = pokemon_data["name"]
        return pokemon_name
    else:
        return None
