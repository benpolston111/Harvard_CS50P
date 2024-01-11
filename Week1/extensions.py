nameOfFile = input("File name: ").strip().lower()

def main():
    if nameOfFile.endswith(".gif"):
        print("image/gif")
    elif nameOfFile.endswith(".jpg"):
        print("image/jpeg")
    elif nameOfFile.endswith(".jpeg"):
        print("image/jpeg")
    elif nameOfFile.endswith(".png"):
        print("image/png")
    elif nameOfFile.endswith(".pdf"):
        print("application/pdf")
    elif nameOfFile.endswith(".txt"):
        print("text/plain")
    elif nameOfFile.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()

