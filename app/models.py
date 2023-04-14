import requests

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.data = self._get_pokemon_data(name)

    def _get_pokemon_data(self, name):
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        data = response.json()
        return data

    def get_image_url(self):
        return self.data["sprites"]["front_shiny"]