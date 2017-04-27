import sys
import MeCab as mc
import wn
from pprint import pprint
from random import choice

#/usr/local/lib/mecab/dic/ipadic/dicrc に下の3行を追加
#
#; test
#node-format-test = %M %f[0]\n
#unk-format-test = %M %f[0]\n

if __name__ == '__main__':

    m = mc.Tagger("-Otest")

    wcs = m.parse(input()).split("\n")
    wcs = [w.split() for w in wcs]
    del wcs[-1]

    # print(wcs)

    synonyms_dic = {}

    for _ in range(10):
        for wl in wcs:
            synonyms = wn.getsynonyms(*wl)
            synonyms.add(wl[0])
            synonyms_dic[wl[0]] = synonyms
            print(choice(list(synonyms)), end="")
            if (wl[0].encode("utf-8").isalpha()):
                print(" ", end="")
        print()

    pprint(synonyms_dic)
