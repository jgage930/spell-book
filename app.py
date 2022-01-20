from flask import Flask, render_template
import requests

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

if __name__ == '__main__':
    app.run(debug=True)