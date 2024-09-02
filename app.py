from flask import Flask
from objects import HTMLElement, HTMLDocument
from website_jobs import create_base_website

app = Flask(__name__)

@app.route("/")
def home_page():
    return str(create_base_website())