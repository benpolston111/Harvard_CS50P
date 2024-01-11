def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dolRepl = d.replace("$","")
    d = float(dolRepl)
    return d



def percent_to_float(p):
    perRepl = p.replace("%","")
    p = float(perRepl)
    return p / 100


main()
