#-*- coding: utf-8 -*-

import jieba
import jieba.analyse
import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import multiprocessing

jieba.load_userdict("usrdic.txt")

def words_seg(inputFile, outputFile):
    stopwords = {}
    fstop = open('stopwords.txt', 'r')
    for eachWord in fstop:
        stopwords[eachWord.strip()] = eachWord.strip()
    fstop.close()
    fin = open(inputFile, 'r')
    fout = open(outputFile, 'w')
    jieba.enable_parallel(2)
    for eachLine in fin:
        line = eachLine.strip()
        wordList = list(jieba.cut(line))
        outStr = ''
        for word in wordList:
            if word not in stopwords:
                outStr += word
                outStr += ' '
        fout.write(outStr.strip() + '\n')
    fin.close()
    fout.close()

# def model_estab():
#     inp = 'xgk_seg.txt'
#     outp1 = 'xgk_text.model'
#     outp2 = 'xgk_text.vector'
#     model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
#     model.save(outp1)
#     model.wv.save_word2vec_format(outp2, binary=False)

def main():
    words_seg('xgk.txt', 'xgk_seg.txt')
    # model_estab()
    return

if __name__ == '__main__':
    main()