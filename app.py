from flask import Flask
from objects import HTMLElement

app = Flask(__name__)

@app.route("/")
def home_page():
    return str(HTMLElement(
        tag="h1", 
        innerHTML="Hey",
        style="color: cyan;",
        ))