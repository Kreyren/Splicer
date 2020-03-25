from random import choice
from termcolor import cprint

# For Prints
colors = ('green', 'yellow', 'blue', 'magenta')
color = choice(colors)


def consolePrint():
    cprint("""
       _____       _ _          
      / ____|     | (_)         
     | (___  _ __ | |_  ___ ___ 
      \___ \| '_ \| | |/ __/ _ \\
      ____) | |_) | | | (_|  __/
     |_____/| .__/|_|_|\___\___|
            | |                 
            |_|
Running Splice v0.1""", color)
