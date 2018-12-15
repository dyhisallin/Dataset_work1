# coding=utf-8

import codecs
import pandas as pd
import numpy as np
import jieba
import jieba.posseg
import gensim
jieba.load_userdict('usrdic.txt')

def getWordVecs(xgkwords, model):
    name = []
    vecs = []
    for xgkword in xgkwords:
        try:
            if xgkword in model:
                name.append(xgkword)
                vecs.append(model[xgkword])
        except KeyError:
            continue
    a = pd.DataFrame(name, columns=['word'])
    b = pd.DataFrame(np.array(vecs, dtype='float'))
    return pd.concat([a, b], axis=1)


def main():
    xgkData = [w.strip() for w in codecs.open('xgk_seg.txt', 'r', encoding='utf-8').readlines()]
    model = gensim.models.KeyedVectors.load_word2vec_format('wiki_text.vector', binary=False)
    # print(xgkData[0])
    jieba.enable_parallel(2)
    for index in range(len(xgkData)):
        words = xgkData[index]
        words = jieba.cut(words)
        words = list(set(words))
        wordvecs = getWordVecs(words, model)
        data_vecs = pd.DataFrame(wordvecs)
        data_vecs.to_csv('vec/xgk_vec_' + str(index) + '.csv', index=False)
    jieba.disable_parallel()

if __name__ == '__main__':
    main()

