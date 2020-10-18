def sortByDate(dataList):
    return sorted(dataList,key=getDate)

def getDate(data):
    return data["dueDate"]

if __name__ == "__main__":
    l = [{"dueDate":"1/23", "time":1, "type":"sleep"},
        {"dueDate":"4/23", "time":2, "type":"sleep"},
        {"dueDate":"3/18", "time":3, "type":"sleep"},
        {"dueDate":"12/30", "time":4, "type":"sleep"},
        {"dueDate":"1/20", "time":5, "type":"sleep"},
        {"dueDate":"1/23", "time":1, "type":"sleep"},
        {"dueDate":"4/23", "time":2, "type":"sleep"},
        {"dueDate":"3/18", "time":3, "type":"sleep"},
        {"dueDate":"12/30", "time":4, "type":"sleep"},
        ]
    
    for w in range (100000):
        ([a["time"] for a in sortByDate(l)])