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
            print("HI")
            if data["type"] == "fixed":
                status = addEvent(data, "fixed")
                return {"status":status}
            if data["type"] == "flex":
                status = addEvent(data, "flex")
                return {"status":status}
        else:
            return {"Error":"NO DATA TYPE"}

    if request.method == 'GET':
        data = request.json
        if "date" in data.keys():
            schedule = getSchedule(data["date"])
            return {"Schedule": schedule}
        else:
            return {"Info": "NO SCHEDULE FOR THAT DATA"}

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
    print("HELLO")
    if type == "fixed":
        fr.addEventToFile('fixedEvents.json', event)
    elif type == "flex":
        fr.addEventToFile('flexEvents.json', event)
    return "Success"