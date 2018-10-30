# Author      : Zuguang Liu
# Date        : 2018-10-30 00:00:04
# Python Ver  : 3.6
# Description : 

import sys
old_stdout = sys.stdout

log_file = open("message.log","w")

sys.stdout = log_file

print ("this will be written to message.log")

sys.stdout = old_stdout

log_file.close()
