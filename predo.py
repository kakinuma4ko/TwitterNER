import tner
import codecs

for filename in tner.files:
    dataFile = codecs.open(tner.DATAPATH + filename, 'r', 'utf-8-sig')
    tempFile = codecs.open(tner.TEMPPATH + filename+'.temp', 'w', 'utf-8')
    Tnum = 0
    tempFile.write('{"subtext":[')
    for line in dataFile.readlines():
        tner.myLog(str(Tnum))
        if not Tnum == 0:
            tempFile.write(',')
        tempFile.write('{"num":'+str(Tnum)+', "text"'+line.replace(b'{"text"', b''))#.replace()
        Tnum += 1
    print ''
    tempFile.write(']}')
    tempFile.close()
    dataFile.close()
