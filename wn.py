import sys
import sqlite3
from pprint import pprint

clas_dic = {"名詞": "n",
            "動詞": "v",
            "形容詞": "a",
            "副詞": "r"}

con = sqlite3.connect("./wnjpn.db")


def getsynonyms(lemma, clas):
    # print(lemma + ": " + clas, end="")
    synonyms = set()
    try:
        wordids = con.execute("select wordid from word where lemma=? and pos=?", (lemma, clas_dic[clas]))
    except:
        return synonyms

    for wordid in wordids:
        synsets = con.execute("select synset from sense where wordid=?", (wordid[0],))
        for synset in synsets:
            synonyms |= {a[0] for a in con.execute(
                "select word.lemma from sense, word where synset=? and word.lang=? and sense.wordid=word.wordid",
                (synset[0], "eng" if lemma.encode("utf-8").isalpha() else "jpn"))}

    # print(synonyms)
    # print(len(synonyms))

    return synonyms
