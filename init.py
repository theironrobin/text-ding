# Written by Alex Robinson on 3-3-20
import sqlite3
import os
from pathlib import Path

db_path = Path("/home/purism/.purple/chatty/db/chatty-history.db")
smscount_path = Path("/home/purism/Projects/text-ding/SMScount.txt")
conn = sqlite3.connect(str(db_path))
cur = conn.cursor()
f = open(str(smscount_path), "w")
buffer = "select * from chatty_im"
cur.execute(buffer);
sms_count = len(cur.fetchall()) + 1
f.write(str(sms_count))
f.close()
conn.close()

