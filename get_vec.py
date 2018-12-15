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
    model = gensim.models.KeyedVectors.load_word2vec_format('wiki_text.vector', binary=False)
    dataList = ['新能源科学与工程', '光电信息科学与工程', '机械设计制造及其自动化', '车辆工程', '生物制药', '计算机科学与技术', '物联网工程', '数字媒体技术', '数据科学与大数据技术', '机器人工程', '智能电网信息工程', '智能科学与技术', '智能建造', '智能制造工程', '智能医学工程', '航空航天工程', '飞行器设计与工程', '飞行器制造工程', '飞行器动力工程', '飞行器环境与生命保障工程', '飞行器质量与可靠性', '飞行器适航技术', '船舶与海洋工程']
    # print(dataList[0])
    wordvecs = getWordVecs(dataList, model)
    data_vecs = pd.DataFrame(wordvecs)
    data_vecs.to_csv('discipline.csv', index=False)

if __name__ == '__main__':
    main()

