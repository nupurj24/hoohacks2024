import os
from flask import Flask, render_template, request 
from openai import OpenAI
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_completion(prompt,):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )
    return response

@app.route("/assistant")
def home():    
    return render_template("assistant.html")

@app.route("/assistant/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    completion = get_completion(userText)
    bot_response = completion['choices'][0]['message']['content']
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)