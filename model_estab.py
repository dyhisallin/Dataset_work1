# -*- coding : utf-8 -*-
import gensim
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    input = 'xgk_seg.txt'
    output1 = 'xgk_text.model'
    output2 = 'xgk_text.vector'
    model = Word2Vec(LineSentence(input), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save(output1)
    model.wv.save_word2vec_format(output2, binary=False)