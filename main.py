# Written by Alex Robinson on 3-3-20
# Requires vlc to work (sudo apt-get install vlc)
import sqlite3
import os
from pathlib import Path

sound_path = Path("/usr/share/sounds/gnome/default/alerts/")
my_sound = sound_path/"bark.ogg"
bark = "cvlc --play-and-exit " + str(my_sound)

db_path = Path("/home/purism/.purple/chatty/db/chatty-history.db")
conn = sqlite3.connect(str(db_path))
cur = conn.cursor()

def get_sms_count():
    buffer = "select * from chatty_im"
    cur.execute(buffer)
    sms_count = len(cur.fetchall()) + 1
    return str(sms_count)

def compare_sms_counts(new_sms_count):
    f = open("SMScount.txt", "r")
    old_sms_count = f.read()
    f.close()
    if (new_sms_count != old_sms_count):
        # find out if last sms was sent or recieved
        if (last_message_recieved(new_sms_count)):
            os.system(bark)
            os.system(bark)
        update_SMScount(new_sms_count)
    return

# This function finds out if the last sms message in your db was a recieved one,
# as opposed to a sent one which we will ignore and not cause an alert.
def last_message_recieved(x):
    buffer = "select * from chatty_im order by id desc"
    #buffer = "SELECT * FROM chatty_im ORDER BY ID DESC LIMIT 1"
    cur.execute(buffer)
    # grab the second column which shows status. 1 for recieved -1 for sent.
    status = cur.fetchone()
   # print(str(status))
   # print(str(status[2]))
    if str(status[2]) == "1":
        return True
    else: 
        return False

def update_SMScount(my_sms_count):
    f = open("SMScount.txt", "w")
    sms_count = my_sms_count
    f.write(sms_count)
    print("SMScount updated")
    return

compare_sms_counts(get_sms_count())

#print(last_message_recieved())

conn.close()
