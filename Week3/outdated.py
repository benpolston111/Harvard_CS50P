months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
        print(y,m.zfill(2),d.zfill(2), sep="-")

def val_check():
    if int(m) <= 12 and int(d) <= 31:
        return True

while True:
    date = input("Date: ")

    try:
        if "/" in date:
            m, d, y = date.split("/")
            if val_check():
                main()
                break
        elif "," in date:
                m, d, y = date.split(" ")
                m = months.index(m) + 1
                m = str(m)
                d = d.replace(",","")
                if val_check():
                    main()
                    break
    except:
        pass