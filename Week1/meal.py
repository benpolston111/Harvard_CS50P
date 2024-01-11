def main():
    time = input("What time is it?: ")

    newTime = convert(time)

    if newTime >= 7.0 and newTime <= 8.0:
        print("breakfast time")
    elif newTime >= 12.0 and newTime <=13.0:
        print("lunch time")
    elif newTime >= 18.0 and newTime <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    newTime = float(hours) + float(minutes) / 60
    return newTime

if __name__ == "__main__":
    main()
