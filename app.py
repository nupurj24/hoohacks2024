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


@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = "Hello! Of course, I'd be happy to help you with recycling ideas for your plastic container from a restaurant. Here are a few sustainable solutions you can consider: Reuse for Food Storage: \n 1. Wash the plastic container thoroughly and reuse it for storing leftovers or meal prepping. This will help reduce waste and save money on purchasing new storage containers. \n 2. Organizing Supplies: Use the container to store small items like buttons, craft supplies, office supplies, or even as a travel case for jewelry or toiletries. It can help keep your space more organized and clutter-free. \n 3. DIY Plant Pot: With a few drainage holes added at the bottom, your plastic container can make a great plant pot for small herbs or succulents. This can add a touch of greenery to your home while repurposing the container. \n 4. Art and Craft Projects: Get creative and upcycle the plastic container into a DIY project. You can paint it, decorate it with washi tape or stickers, and turn it into a pen holder, mini planter, or even a bird feeder. \n 5. Donate or Share: If you have excess plastic containers, consider donating them to local community centers, schools, or food banks where they can be repurposed or reused. Sharing with friends or family who might have a use for them is also a great way to prevent them from going to waste. \n Remember, always check with your local recycling guidelines to see if plastic containers are accepted in your recycling program. If not, exploring these alternative ways to reuse or repurpose them is a sustainable and eco-friendly option. Let me know if you need more recycling ideas or tips!" 
    return response

if __name__ == '__main__':
    app.run(debug=True)