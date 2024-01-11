from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

fonts = figlet.getFonts()

commands = ["-f", "--font"]


if len(sys.argv) == 1:
    fig_font = random.choice(fonts)

elif len(sys.argv) == 3 and sys.argv[2] in fonts and sys.argv[1] in commands:
    fig_font = sys.argv[2]

else:
    sys.exit("Invalid usage")

text = input("Input: ")
figlet.setFont(font=fig_font)
print(figlet.renderText(text))
