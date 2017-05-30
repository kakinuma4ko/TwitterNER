import tner
import json
import codecs
import re

for filename in tner.files:
    jsonFile = codecs.open(tner.JSONPATH + filename + '.json', 'r', 'utf-8-sig')

    atNum = 0
    httpNum = 0
    tagNum = 0

    subJson = json.load(jsonFile)
    jsonTextArray = subJson['subtext']

    for jsonText in jsonTextArray:
        tner.Log(filename + '|' + str(jsonText['num'] + 1) + '/' + str(len(jsonTextArray)))
        if str(jsonText['text']).find('@') != -1:
            atNum += 1
            # print '@'
        if str(jsonText['text']).find('#') != -1:
            tagNum += 1
            # print '#'
        if len(jsonText['http']) > 0:
            httpNum += 1
            # print 'http'
            # print jsonText['text']
    print '@' + str(atNum) + '#' + str(tagNum) + 'http' + str(httpNum)
    
