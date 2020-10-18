import json

def readFile(file):
    try:
        with open(file) as json_file:
            jsonData = json.load(json_file)
    except IOError:
        with open(file,'w') as json_file:
            json_file.write("[]")
    with open(file) as json_file:
            jsonData = json.load(json_file)
    return jsonData

def addEventToFile(file, event):
    json_data = readFile(file)
    
    if(len(json_data) == 0):
        json_data.append(event)
    elif(json_data[-1]["deadline"] <= event["deadline"]):
        json_data.append(event)
    elif(json_data[0]["deadline"] >= event["deadline"]):
        json_data.insert(0, event)
    else:
        for i in range(len(json_data[:-1])):
            loc = json_data[i]["deadline"]
            nloc = json_data[i+1]["deadline"]
            val = event["deadline"]
            if (loc <= val) and (val <= nloc):
                json_data.insert(i+1, event)
                break

    with open(file,'w') as outfile:
        json.dump(json_data, outfile)
    
if __name__ == "__main__":
    addEventToFile('events.json',
        {"name": "event", 
        "length": 80,
        "deadline": "1/22",
        "type": "flex"})
    addEventToFile('events.json',
        {"name": "event", 
        "length": 80,
        "deadline": "1/25",
        "type": "flex"})