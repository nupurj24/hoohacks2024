from flask import Flask, render_template, request
from backend.ecorestaurants import EcoRestaurants
import openai, os

app = Flask(__name__)
openai.api_key  = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ecoeater')
def ecoeater():
    json_ecorestaurants = EcoRestaurants().getEcorestaurantsJSON()
    return render_template('ecoeater.html', ecorestaurants=json_ecorestaurants)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        
    )
    return response.choices[0].message["content"]

@app.route("/ecobuddy")
def ecobuddy():    
    return render_template("ecobuddy.html")

@app.route("/ecobuddy/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    return response

if __name__ == '__main__':
    app.run(debug=True)