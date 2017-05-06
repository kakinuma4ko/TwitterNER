# -*- coding: UTF-8 -*-
import nltk


# 载入序列化对象
chunker = nltk.data.load('chunkers/maxent_ne_chunker/english_ace_multiclass.pickle')

# 最大熵分类器
maxEnt = chunker._tagger.classifier()

def maxEnt_report():
    maxEnt = chunker._tagger.classifier()
    print 'These are the labels used by the NLTK\'s NEC...'
    print maxEnt.labels()
    print ''

    print 'These are the most informative features found in the ACE corpora...'
    maxEnt.show_most_informative_features()

def ne_report(sentence, report_all=False):

    # 词性标记
    tokens = nltk.word_tokenize(sentence)
    tokens = nltk.pos_tag(tokens)

    tags = []
    for i in range(0, len(tokens)):
        featureset = chunker._tagger.feature_detector(tokens, i, tags)
        tag = chunker._tagger.choose_tag(tokens, i, tags)
        if tag != 'O' or report_all:
            print '\nExplanation on the why the word \'' + tokens[i][0] + '\' was tagged:'
            featureset = chunker._tagger.feature_detector(tokens, i, tags)
            maxEnt.explain(featureset)
        tags.append(tag)

ne_report("Thank you Indiana, we were just projected to be the winner. We have won in every category. You are very special people-I will never forget!")
