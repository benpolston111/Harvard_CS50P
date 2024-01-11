def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #between 2-6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    #starts with 2 letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    #numbers must be at the end & first must not be 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    #no punctuation
    for c in s:
        if c in ["."," ","!","?"]:
            return False

    #all tests passed
    return True




main()
