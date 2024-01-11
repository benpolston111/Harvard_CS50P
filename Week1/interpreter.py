expression = input("Expression: ")

x, y, z = expression.split(" ")

numx = float(x)
numz = float(z)

def main():
    if y == "+":
        print(numx + numz)
    elif y == "-":
        print(numx - numz)
    elif y == "*":
        print(numx * numz)
    elif y == "/":
        print(numx / numz)

main()
