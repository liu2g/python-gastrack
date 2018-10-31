# Author      : Zuguang Liu
# Date        : 2018-10-30 19:02:59
# Python Ver  : 3.6
# Description : 

import sqlite3

sqlite_file = 'my_first_db.sqlite' 
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

conn.commit()
conn.close()