import fileOperations as fr
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mainRoute():
    return render_template("main.html")

@app.route('/schedule', methods=['POST','GET'])
def schedule():
    if request.method == 'POST':
        data = request.json
        returnValue = False;
        if "type" in data.keys():
            if data["type"] == "fixed":
                print("NEW FIXED EVENT")
                return addEvent(data, "fixed")
               
            if data["type"] == "flex":
                print("NEW FLEX EVENT")
                return addEvent(data, "fixed")
        else:
            return {"Error":"NO DATA TYPE"}

    if request.method == 'GET':
        data = request.json
        if "date" in data.keys():
            schedule = getSchedule(data["date"])
            return {"Schedule": schedule}
        else:
            return {"Info": "NO SCHEDULE FOR THAT DATA"}
        return{}

def getSchedule(date):
    return [{"name":"testEvent", 
        "startTime":900, 
        "endTime": 1000},
        {"name":"testEvent", 
        "startTime":1000, 
        "endTime":1015},
        {"name":"testEvent", 
        "startTime":1015, 
        "endTime":1130}]

def addEvent(event, type):
    if type == "fixed":
        fr.addEventToFile('fixedEvents.json', event)
    elif type == "flex":
        fr.addEventToFile('flexEvents.json', event)
    return "Item Added"