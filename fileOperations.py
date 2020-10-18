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