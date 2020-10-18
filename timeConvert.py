def addTime(startTime, increment):
    time = startTime + increment
    extraMinutes = int(str(time)[-2:])
    print(extraMinutes)
    hour = startTime // 100
    print(hour)
    if extraMinutes >= 60:
        hour +=  extraMinutes//60 + 1
        extraMinutes -= 60*(extraMinutes//60 + 1)
        time = (hour)*100+extraMinutes
    return time


def diffTime():
    return 0

if __name__ == "__main__":
    print(addTime(1000, 90))