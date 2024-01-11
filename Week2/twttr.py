twit_case = input("Input: ")

v = ["a","e","i","o","u"]

print("Output: ", end="")

for c in twit_case:
    if c.casefold() not in v:
        print(c, end="")

print()