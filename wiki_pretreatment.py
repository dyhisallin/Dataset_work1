# -*- coding: utf-8  -*-

import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    input, output1 = sys.argv[1:3]
    space = " "
    i = 0
    output2 = open(output1, 'w')
    wiki =WikiCorpus(input, lemmatize=False, dictionary=[])
    for text in wiki.get_texts():
        output2.write(space.join(text) + "\n")
        i = i+1

    output1.close()
    output2.close()
