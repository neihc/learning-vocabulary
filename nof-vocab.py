import gi
gi.require_version('Notify', '0.7')
from gi.repository import GObject
from gi.repository import Notify
import json
import random
import time
import os

class Nofti(GObject.Object):
    def __init__(self):

        super(Nofti, self).__init__()
        # lets initialise with the application name
        Notify.init("vocab_name")

    def send_notification(self, title, text, file_path_to_icon=""):

        n = Notify.Notification.new(title, text, file_path_to_icon)
        n.show()

nof = Nofti()

with open("vocab-data.json") as data_file:
    data = json.load(data_file)

while True:
    word = random.choice(data)
    title = "Hey! Word for this session here!"
    content = "<i><b>"+word['word']+"</b></i> (+"+word['type']+") \n"+word['mean']
    nof.send_notification(title, content, "~/icon.png")
    os.system("spd-say 'You have new word, listen!'")
    time.sleep(3)
    os.system("spd-say "+word['word'])
    time.sleep(1)
    os.system("spd-say 'It means "+word['mean']+"'")
    time.sleep(30*60)
