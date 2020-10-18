fixed = [{}]
fixed.append({"name": "class3", "start": 1000, "end": 1030}) #last elem will not show up... so adding an element at the end
flexy = [{}] 
flexy.append({"name2": "hw3", "length": 50, "dueDate": 0 })
finalSchedule = list()
index = 0
timeBlock = 0
while index < len(fixed)-1: #missing the last elem in fixed
    finalEvent = {
                "name": "",
                "priority": "",
                "length": 0,
                "start": 0,
                "end": 0,
                "dueDate": 0,
            }
    finalEvent = {"name":fixed[index]["name"],
        "priority": "fixed", 
        "length": abs(fixed[index]["start"] - fixed[index]["end"]), 
        "start":fixed[index]["start"], "end":fixed[index]["end"]}

    finalSchedule.append(finalEvent)
    timeBlock = fixed[index+1]["start"] - fixed[index]["end"]
    for event in flexy:
        if event["length"] <= timeBlock:
            finalEvent = {}
            finalEvent["name"] = event["name2"]
            finalEvent["priority"] = "flex"
            finalEvent["length"] = event["length"]
            finalEvent["start"] = finalSchedule[-1]["end"]
            finalEvent["end"] = finalEvent["start"] + event["length"] #all done in milliseconds
            finalEvent["dueDate"] = event["dueDate"]
            finalSchedule.append(finalEvent)
            timeBlock -= event["length"]
    index+=1