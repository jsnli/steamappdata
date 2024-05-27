from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>index()</p>"

@app.route("/about")
def about():
    return "<p>about()</p>"