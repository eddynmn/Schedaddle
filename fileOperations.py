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

    if (len(json_data) == 0):
        json_data.append(event)
    elif (event["deadline"] >= json_data[-1]["deadline"]):
        json_data.append(event)
    else:
        for i in range(len(json_data[:-1])):
            val = json_data[i]["deadline"]
            nextVal = json_data[i+1]["deadline"]
            deadline = event["deadline"]
            print(deadline, val)
            if (deadline <= val):
                json_data.insert(i, event)
                break
            elif (val <= deadline) and (deadline <= nextVal):
                json_data.insert(i+1, event)
                break
    

    with open(file,'w') as outfile:
        json.dump(json_data, outfile)
        return True
    
    return False

if __name__ == "__main__":
    addEventToFile('events.json',
        {"name": "event", 
        "length": 80,
        "deadline": "1/26",
        "type": "flex"})
    addEventToFile('events.json',
        {"name": "event", 
        "length": 80,
        "deadline": "1/22",
        "type": "flex"})