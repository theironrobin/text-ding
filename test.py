#!/usr/bin/python3

import os
from pathlib import Path

sound_path = Path("/usr/share/sounds/gnome/default/alerts/")
my_sound = sound_path/"bark.ogg"
bark = "cvlc --play-and-exit " + str(my_sound)
os.system(bark)

