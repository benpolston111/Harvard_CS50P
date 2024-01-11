def main():
    text = input()
    newText = convert(text)
    print(newText)

def convert(text):
    emoji = text.replace(":)", "🙂").replace(":(", "🙁")
    return emoji

main()
