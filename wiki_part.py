# -*- coding: utf-8  -*-

import jieba
import jieba.analyse
import codecs

if __name__ == '__main__':
    f = codecs.open('wiki_simp.txt', 'r', encoding='utf8')
    target = codecs.open('wiki_simp_seg.txt', 'w', encoding='utf8')

    line = f.readline()
    while line:
        seg_list = jieba.cut(line)
        line_seg = ' '.join(seg_list)
        target.writelines(line_seg)
        line = f.readline()
    f.close()
    target.close()