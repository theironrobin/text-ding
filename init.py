# Written by Alex Robinson on 3-3-20
import sqlite3
import os
from pathlib import Path

sound_path = Path("/usr/share/sounds/gnome/default/alerts/")
my_sound = sound_path/"bark.ogg"
db_path = Path("/home/purism/.purple/chatty/db/chatty-history.db")
conn = sqlite3.connect(str(db_path))
cur = conn.cursor()
f = open("SMScount.txt", "w")
buffer = "select * from chatty_im"
cur.execute(buffer);
sms_count = len(cur.fetchall()) + 1
f.write(str(sms_count))
f.close()
conn.close()

