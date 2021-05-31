from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/movies')
def movies():
    movieList = [{'name': 'Analyze This', 'year': 1999, 'genre': 'Comedy', 'rating':'6.7/10'}, {'name': 'Analyze This', 'year': 1999, 'genre': 'Comedy', 'rating':'*'}];
    return json.dumps(movieList)

@app.route('/favicon.ico')
def favicon():
    return ''

app.run(host='127.0.0.1', port=8080)