import time
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def get_current_time():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return {"data": "Goodbye World!!"}

@app.route('/schedule', methods=['POST','GET'])
def foundScheule():
    if request.method == 'POST':
        a = request.json
        return{"data": a[::-1]}