from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/movies')
def movies():
    movieList = []
#var movietdst = '[{"name": "Analyze This", "year": 1999, "genre": "Comedy", "rating":"6.7/10"}, {"name": "Analyze This", "year": 1999, "genre": "Comedy", "rating":"*"}]';
    return ""

app.run(host='127.0.0.1', port=8080)