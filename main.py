# Written by Alex Robinson on 3-3-20
# Requires vlc to work (sudo apt-get install vlc)
import sqlite3
import os
from pathlib import Path

sound_path = Path("/usr/share/sounds/gnome/default/alerts/")
my_sound = sound_path/"bark.ogg"
db_path = Path("/home/purism/.purple/chatty/db/chatty-history.db")




bark = "cvlc --play-and-exit " + str(my_sound)



os.system(bark)

