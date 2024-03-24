from flask import Flask, render_template
from backend.ecorestaurants import EcoRestaurants

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ecoeater')
def ecoeater():
    json_ecorestaurants = EcoRestaurants().getEcorestaurantsJSON()
    return render_template('ecoeater.html', ecorestaurants=json_ecorestaurants)

if __name__ == '__main__':
    app.run(debug=True)