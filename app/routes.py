from flask import redirect, render_template, redirect, url_for
from app.forms import PokemonForm
import requests
from app import app

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def index():
    form = PokemonForm()
    if form.validate_on_submit():
        return redirect(url_for('pokemon_search', pokemon_name=form.pokemon_name.data))
    return render_template('index.html', form=form)

@app.route('/search/<pokemon_name>', methods=['GET', 'POST'])
def pokemon_search(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
    if response.ok:
        data = response.json()
        name = data['name'].capitalize()
        ability = data["abilities"][0]["ability"]["name"]
        base_experience = data['base_experience']
        image_url  = data["sprites"]["front_shiny"]
        stats = data['stats']
        for stat in stats:
            if stat['stat']['name'] == 'attack':
                attack = stat['base_stat']
            elif stat["stat"]["name"] == "defense":
                defense = stat['base_stat']
            elif stat["stat"]["name"] == "hp":
                hp = stat['base_stat']
        return render_template('pokemon.html', name=name, ability=ability, base_experience=base_experience, image_url=image_url, attack=attack, defense=defense, hp=hp)
    else:
        # Redirect back to home page with error message
        return redirect(url_for('index', error_message=f'No pokemon found with name "{pokemon_name}"'))






# @app.route('/')
# def home():
#     form = PokemonForm()
#     if form.validate_on_submit():
#         # Redirect to the /search route with the entered pokemon name as parameter
#         return redirect(url_for('pokemon_search', pokemon_name=form.pokemon_name.data))
#     return render_template('index.html', form=form)

# @app.route('/search', methods = ['GET', 'POST'])
# def pokemon_search():
#     pokemon_name = form.pokemon_name.data.lower()
#     response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
#     if response.ok:
#         data = response.json()
#         name = data['name'].capitalize()
#         image_url  = data["sprites"]["front_shiny"]
#         stats = data['stats']
#         for stat in stats:
#             if stat['stat']['name'] == 'attack':
#                 attack = stat['base_stat']
#             elif stat["stat"]["name"] == "defense":
#                 defense = stat["base_stat"]
#             elif stat["stat"]["name"] == "hp":
#                 hp = stat["base_stat"]
#         return render_template('pokemon.html', name=name, image_url=image_url, attack=attack, defense=defense, hp=hp)
#     else:
#         form.pokemon_name.errors.append(f'No pokemon found with name "{pokemon_name}"')
# return render_template('pokemon.html')
