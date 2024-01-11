answer = input("What is the answer to the Great Question of Life, the Universe, and Everything?: ").lower().strip()

correct = ["42","forty-two","forty two"]

if answer in correct:
    print("Yes")
else:
    print("No")
