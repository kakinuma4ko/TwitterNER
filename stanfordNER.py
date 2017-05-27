import tner
import codecs
import json
from nltk.tag import StanfordNERTagger

stNERTagger = StanfordNERTagger('./StanfordNER/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/suntian/Developer/NLP/StanfordNER/stanford-ner-2016-10-31/stanford-ner.jar')

print '==================='
print 'stanfordNER'

for filename in tner.files:
    jsonFile = codecs.open(tner.JSONPATH + filename + '.json', 'r', 'utf-8')
    stfOutFile = codecs.open(tner.STFPATH + filename + '.stanfordNERTag', 'w', 'utf-8-sig')
    subJson = json.load(jsonFile)
    jsonTextArray = subJson['subtext']
    for jsonText in jsonTextArray:
        tagged = stNERTagger.tag(jsonText['text'].split()) # doctest: +SKIP
        tner.Log(filename + '|' + str(jsonText['num']) + '/' + str(len(jsonTextArray)))
        for tag in tagged:
            stfOutFile.write(tag[0])
            if tag[1] == 'LOCATION':
                stfOutFile.write(' STFNER\n')
            else:
                stfOutFile.write(' O\n')
