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

import json
import re

for filename in tner.files:
    tempFile = codecs.open(tner.TEMPPATH + filename+'.temp', 'r', 'utf-8')
    jsonFile = codecs.open(tner.JSONPATH + filename+'.json', 'w', 'utf-8')

    subJson = json.load(tempFile)
    jsonTextArray = subJson['subtext']

    for jsonText in jsonTextArray:
        tner.myLog(str(jsonText['num']))
        httpsPattern = re.compile('https://t.co/\w*', re.S)
        items = re.findall(httpsPattern, jsonText['text'])
        httpsArray = []
        for item in items:
            jsonText['text'] = jsonText['text'].replace(item, b'')
            httpsArray.append(item)
        # print jsonText['text']
        jsonText['http'] = httpsArray

    json.dump(subJson,jsonFile)
