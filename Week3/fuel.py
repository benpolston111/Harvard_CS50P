def main():
    x = handler("Fraction: ")
    if x <= 1:
        print("E")
    if 99 <= x < 101:
        print("F")
    if 1 < x < 99:
        print(x, "%", sep="")

def handler(prompt):
    while True:
        try:
            fuel = input(prompt)
            x, y = fuel.split("/")
            fuel_gauge = round(int(x)/int(y)*100)

            if int(y) == 0 or int(x) > int(y):
                continue
            elif fuel_gauge <= 1:
                return fuel_gauge
            elif 99 <= fuel_gauge < 101:
                return fuel_gauge
            else:
                return fuel_gauge

        except(ValueError, ZeroDivisionError):
            pass

main()