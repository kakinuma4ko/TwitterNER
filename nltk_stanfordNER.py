from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('/Users/suntian/Developer/NLP/StanfordNER/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/suntian/Developer/NLP/StanfordNER/stanford-ner-2016-10-31/stanford-ner.jar')
print st.tag('Rami Eid is studying at Stony Brook University in NY'.split()) # doctest: +SKIP
