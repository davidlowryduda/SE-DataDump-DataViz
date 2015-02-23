#!/usr/bin/env python
# encoding: utf-8

import xml.sax
import xmlparser

from nltk import sent_tokenize, word_tokenize

from IPython.display import clear_output
import sys


class MSEStatistic():
    """Handler for statistic generation."""

    def __init__(self, ATTRIBUTES, FILE):
        self.d = {}
        self.total = 0
        self.counter = 0
        self.ATTRIBUTES = ATTRIBUTES
        self.FILE = FILE

    def zipf(self, body):
        for l in body:
            self.total += 1
            if l in self.d:
                self.d[l] += 1
            else:
                self.d[l] = 1

    def zipf_words(self, body):
        #body = body.encode("utf8", 'ignore')
        #sents = sent_tokenize(body)
        #words_arrays = [word_tokenize(s) for s in sents]
        #words = [w for s in words_arrays for w in s]
        words = [word.lower() for s in sent_tokenize(body) for word in word_tokenize(s)]
        for w in words:
            if w in self.d:
                self.d[w] += 1
            else:
                self.d[w] = 1
        self.total += 1
        if self.total%100 == 0:
            clear_output()
            print self.total, "rows processed",
            sys.stdout.flush()

    def counter(self, body):
        self.counter += 1
        if self.total%100 == 0:
            clear_output()
            print self.counter, "rows counted",
            sys.stdout.flush()


def main():
    """Returns total, d"""
    parser = xml.sax.make_parser()
    stats = MSEStatistic(ATTRIBUTES=["Body"], FILE="Posts.xml")
    Handler = xmlparser.MSEHandler(details=stats.ATTRIBUTES, func=stats.zipf_words)
    parser.setContentHandler(Handler)
    parser.parse(stats.FILE)
    print stats.total
    print stats.d
    return stats.total, stats.d


def do_counter():
    parser = xml.sax.make_parser()
    stats = MSEStatistic(ATTRIBUTES=["Body"], FILE="Posts.xml")
    Handler = xmlparser.MSEHandler(details=stats.ATTRIBUTES, func=stats.counter)
    parser.setContentHandler(Handler)
    parser.parse(stats.FILE)
    print stats.total

if __name__ == '__main__':
    main()
