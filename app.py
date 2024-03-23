from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ecoeater')
def ecoeater():
    return render_template('ecoeater.html')

if __name__ == '__main__':
    app.run(debug=True)