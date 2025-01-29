from pydoc import text
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

texts = ["Lorem ipsum odor amet, consectetuer adipiscing elit.",
    "Malesuada erat aptent torquent aliquam vulputate sodales dui.",
    "Phasellus potenti tellus vestibulum feugiat semper lobortis natoque potenti."]

@app.route('/first')
def first():
    return texts[0]

@app.route('/second')
def second():
    return texts[1]

@app.route('/third')
def third():
    return texts[2]