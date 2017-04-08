import json
import random
from termcolor import cprint

with open("5000-english-words.json") as data_file:
    data = json.load(data_file)

word = random.choice(data)
cprint("Word for this session:  ", end="", attrs=['bold'])
cprint(word['word'], "cyan", end="")
cprint(" (", end = "")
cprint(word['type'], "yellow", end="")
cprint(")")
cprint("Meaning:                ", end="", attrs=['bold'])
cprint(word['mean'], "green")
