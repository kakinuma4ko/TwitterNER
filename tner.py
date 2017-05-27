import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

files = []
for file in os.listdir(DATAPATH):
    if file[0] != '.':
        files.append(file)

def myLog(str):
    sys.stdout.write('\r')
    sys.stdout.write(str)
    sys.stdout.flush()
