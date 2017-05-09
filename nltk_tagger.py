# -*- coding: UTF-8 -*-
import nltk
import codecs
import json
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# from nltk.book import *
DATAPATH = '/Users/suntian/Developer/NLP/data/data/'
RESULTPATH = DATAPATH + '../result/'

def myLog(str):
    sys.stdout.write('\r')
    sys.stdout.write(str)
    sys.stdout.flush()


def tagfromfile(filename):

    print '=================================\n'+filename

    print 'write temp'

    dataFile = codecs.open(DATAPATH + filename, 'r', 'utf-8-sig')
    tempFile = codecs.open(RESULTPATH + filename+'.temp', 'w', 'utf-8')
    Tnum = 0
    tempFile.write('{"subtext":[')
    for line in dataFile.readlines():
        myLog(str(Tnum))
        if not Tnum == 0:
            tempFile.write(',')
        tempFile.write('{"num":'+str(Tnum)+', "text"'+line.replace(b'{"text"', b''))#.replace()
        Tnum += 1
    print ''
    tempFile.write(']}')
    tempFile.close()
    dataFile.close()

    print 'write corpus'

    tempFile = codecs.open(RESULTPATH+filename+'.temp', 'r', 'utf-8')
    corpusFile = codecs.open(RESULTPATH+filename+'.corpus', 'w', 'utf-8')
    nerCorpusFile = codecs.open(RESULTPATH+filename+'.ner.corpus', 'w', 'utf-8')
    textFile = codecs.open(RESULTPATH+filename+'.text', 'w', 'utf-8')

    subJson = json.load(tempFile)

    jsonTextArray = subJson['subtext']
    for jsonText in jsonTextArray:
        myLog(str(jsonText['num']))
        # print jsonText['text']
        textFile.write(jsonText['text'])
        textFile.write('\n')

        httpsPattern = re.compile('https://t.co/\w*', re.S)
        items = re.findall(httpsPattern, jsonText['text'])
        httpsArray = []
        for item in items:
            jsonText['text'] = jsonText['text'].replace(item, b'')
            httpsArray.append(item)
        # print jsonText['text']
        jsonText['http'] = httpsArray
        tokenSents = nltk.sent_tokenize(jsonText['text'])
        for sent in tokenSents:
            words = nltk.word_tokenize(sent)
            tags = nltk.pos_tag(words)
            ner = nltk.ne_chunk(tags)
            i = 0
            # print sent
            spaceInNer = []
            for j in range(0,len(ner)):
                spaceInNer.append(len(re.findall(' ', str(ner[j]))))
            for tag in tags:
                nerCorpusFile.write(tag[0])
                nerCorpusFile.write(' ')
                nerCorpusFile.write(tag[1])
                nerCorpusFile.write(' ')

                corpusFile.write(tag[0])
                corpusFile.write(' ')
                corpusFile.write(tag[1])
                corpusFile.write(' ')
                corpusFile.write('\n')


                if spaceInNer[i] > 1:
                    if str(ner[i]._label).startswith('GPE'):
                        nerCorpusFile.write(ner[i]._label)
                    else:
                        nerCorpusFile.write('NER')
                    spaceInNer[i] -= 1
                    i -= 1
                else:
                    if hasattr(ner[i],'_label'):
                        if str(ner[i]._label).startswith('GPE'):
                            nerCorpusFile.write(ner[i]._label)
                        else:
                            nerCorpusFile.write('NER')
                    else:
                        nerCorpusFile.write('O')
                i += 1
                nerCorpusFile.write('\n')
    tempFile2 = codecs.open(RESULTPATH + filename + '.temp2', 'w', 'utf-8')
    json.dump(jsonTextArray,tempFile2)
    tempFile2.close()
    print ''

print os.listdir(DATAPATH)
for filename in os.listdir(DATAPATH):
    if filename[0] != '.':
        tagfromfile(filename)

