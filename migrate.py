import sqlite3
from datetime import datetime
conn = sqlite3.connect('database.sqlite3')

c = conn.cursor()

# Create table
c.execute('''create table logs (updated datetime, point int)''')

# conn = sqlite3.connect('database.sqlite3')
# c.commit()

c.execute("select * from logs;")
c.close()
