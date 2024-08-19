from flask import Flask
from objects import HTMLElement, HTMLDocument

app = Flask(__name__)

@app.route("/")
def home_page():
    return str(
        HTMLDocument(body = [
            HTMLElement(
                    tag="h1", 
                    innerHTML="Hey",
                    style="color: green;",
                    ),
            HTMLElement(
                    tag="h2", 
                    innerHTML="How is it going?",
                    style="color: cyan;",
                    ),
        ])
    )