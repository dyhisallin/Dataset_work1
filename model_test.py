#-*- coding: utf-8 -*-
import gensim

if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('wiki_text.model')
    # model = gensim.models.Word2Vec.load('xgk_text.model')
    word = model.most_similar(u"软件")
    for t in word:
        print(t[0], t[1])
    # word = model.most_similar(positive=[u'工科', u'计算机'], negative=[u'编程'])
    # for t in word:
    #     print(t[0], t[1])
    #
    # vocab = model.wv.vocab
    # word_vector = {}
    # for word in vocab:
    #     word_vector[word] = model[word]

    # print(model['计算机'])


