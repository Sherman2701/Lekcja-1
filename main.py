from flask import Flask 
import random

facts=[
    "W Stanach Zjednoczonych nie ma języka urzędowego.",
    "W kasynach w Las Vegas nie ma zegarów ani okien.",
    " Koty w starożytnym Egipcie były uznawane za święte.",
    "Najwięcej rozmów telefonicznych odbywa się w Dzień Matki.",
    "W 1967 roku wieża Eiffla miała być przeniesiona do Kanady.",

]
app = Flask(__name__)

@app.route("/")
def main_site():
    return f'<a href="/random_fact">Zobacz losowy fakt!</a>'

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(facts)}</p>'

app.run(debug=True)