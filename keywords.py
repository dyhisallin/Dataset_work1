# coding=utf-8
# 采用Word2Vec词聚类方法抽取关键词1——获取文本词向量表示
import sys, codecs
import pandas as pd
import numpy as np
import jieba
import jieba.posseg
import gensim
jieba.load_userdict('usrdic.txt')

# 返回特征词向量
def getWordVecs(wordList, model):
    name = []
    vecs = []
    for word in wordList:
        word = word.replace('\n', '')
        try:
            if word in model:  # 模型中存在该词的向量表示
                name.append(word.encode('utf8'))
                vecs.append(model[word])
        except KeyError:
            continue
    a = pd.DataFrame(name, columns=['word'])
    b = pd.DataFrame(np.array(vecs, dtype='float'))
    return pd.concat([a, b], axis=1)

# 数据预处理操作：分词，去停用词，词性筛选
# def dataPrepos(text, stopkey):
#     l = []
#     pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
#     # seg = jieba.posseg.cut(text)  # 分词
#     for word in text:
#         if word not in l and word not in stopkey and flag in pos:  # 去重 + 去停用词 + 词性筛选
#             # print i.word
#             l.append(i.word)
#     return l


# 根据数据获取候选关键词词向量
def buildAllWordsVecs(data, stopkey, model):

    # idList, titleList, abstractList = data['id'], data['title'], data['abstract']
    # words = dataPrepos(data, stopkey)
    words = data  # 数组元素去重,得到候选关键词列表
    for word in words:
        wordvec = getWordVecs(word, model)
        data_vecs = pd.DataFrame(wordvec)
        data_vecs.to_csv('wordvec_' + str(word) + '.csv', index=False)
        print("well done")
    # for index in range(len(idList)):
        # id = idList[index]
        # title = titleList[index]
        # abstract = abstractList[index]
        # l_ti = dataPrepos(title, stopkey)  # 处理标题
        # l_ab = dataPrepos(abstract, stopkey)  # 处理摘要
        # 获取候选关键词的词向量
        # words = np.append(l_ti, l_ab)  # 拼接数组元素

        # words = list(set(words))  # 数组元素去重,得到候选关键词列表
        # wordvecs = getWordVecs(words, model)  # 获取候选关键词的词向量表示
        # # 词向量写入csv文件，每个词400维
        # data_vecs = pd.DataFrame(wordvecs)
        # data_vecs.to_csv('wordvecs_' + str(id) + '.csv', index=False)
        # print("document ", id, " well done.")

def main():
    # # 读取数据集
    # dataFile = 'data/sample_data.csv'
    # data = pd.read_csv(dataFile)
    # 爬取的新工科数据
    xgkData = [w.strip() for w in codecs.open('xgk_seg.txt', 'r', encoding='utf-8').readlines()]
    # 再次整理
    stopkey = [w.strip() for w in codecs.open('stopwords.txt', 'r',encoding='utf-8').readlines()]
    # 载入模型
    input = 'wiki_text.vector'
    model = gensim.models.KeyedVectors.load_word2vec_format(input, binary=False)
    # for line in xgkData:
    # l = []
    # pos = ['n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd']  # 定义选取的词性
    # seg = jieba.posseg.cut(xgkData)  # 分词
    # for i in seg:
    #     if i.word not in l and i.word not in stopkey and i.flag in pos:  # 去重 + 去停用词 + 词性筛选
    #         print(i.word)
    #         l.append(i.word)

    buildAllWordsVecs(xgkData, stopkey, model)

if __name__ == '__main__':
    main()

