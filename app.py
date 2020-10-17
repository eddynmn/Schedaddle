import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_current_time():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return {"data": "Hello World"}
