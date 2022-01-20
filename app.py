from flask import Flask, render_template
import requests
import json
from models.spell import Spell

app = Flask(__name__)
global base_url

def getSpells(level: int) -> list:
    """Calls api and returns any spell of tthe level.  Use 0 for cantrips"""
    base_url = 'https://www.dnd5eapi.co/api/'

    response = requests.get(base_url + f'spells/?level={str(level)}')
    spells = response.json()['results']

    return spells

@app.route('/')
def index():
    # get all spell data
    spells = {}
    for i in range(0, 10):
        spells[str(i)] = getSpells(i)
    
    return render_template('main.html', spells=spells)

@app.route('/<spell_name>')
def spell_view(spell_name):
    # find the spell name and get data from the json file
    spell_data = {}
    with open('data.json', 'r') as f:
        spell_data = json.load(f)

    if spell_name in spell_data:
        # current spell
        my_data = spell_data[spell_name]
        index = my_data['index']
        # get data to put into Spell object
        name = my_data['name']
        desc = ' '.join([str(elem) for elem in my_data['desc']])
        range = my_data['range']
        components = ' '.join([str(elem) for elem in my_data['components']])
        
        if 'material' in my_data:
            material = my_data['material']
        else:
            material = ''

        if my_data['ritual'] == 'false':
            ritual = 'No'
        else:
            ritual = 'Yes'

        duration = my_data['duration']
        
        if my_data['concentration'] == 'false':
            concentration = 'No'
        else:
            concentration = 'Yes'

        casting_time = my_data['casting_time']
        level = my_data['level']
        school = my_data['school']['name']

        spell = Spell(name, desc, range, components, material, ritual, duration, concentration, casting_time, level, school, index)
        return render_template('spell_view.html', spell=spell)
    return render_template('error.html')            



if __name__ == '__main__':
    app.run(debug=True)