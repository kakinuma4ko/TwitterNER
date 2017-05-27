import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

DATAPATH = './data/data/'
JSONPATH = './data/json/'
TEMPPATH = './data/temp/'
STFPATH = './data/stf/'
NLTKPATH = './data/nltk/'

files = []
for file in os.listdir(DATAPATH):
    if file[0] != '.':
        files.append(file)

def Log(str):
    sys.stdout.write('\r')
    sys.stdout.write(str)
    sys.stdout.flush()
