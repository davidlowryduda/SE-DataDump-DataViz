#!/usr/bin/env python
# encoding: utf-8

import xml.sax
#import xmlparser

#from nltk import sent_tokenize, word_tokenize

#from IPython.display import clear_output
#import sys


class MSE_Reference_Handler(xml.sax.ContentHandler):
    def __init__(self, details=[], func=None, output_file="output.xml"):
        self.details = details
        self.func = func
        self.output_file = output_file
        self.data = ""

    def startElement(self, tag, attributes):
        """Activates on opening each row"""
        if (attributes["PostId"] == 1) and (has_keywords(attributes["Tags"])):
            self.data = "<" + tag
            for key in attributes.keys():
                self.data += " " + key + ":" + attributes[key]

    def endElement(self, tag):
        """thing"""
        self.data += " >"
        f = file(self.output_file, "a")
        f.write(self.data)
        f.close()
        self.data = ""


# Helper functions
def has_keywords(body):
    return True

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    Handler = MSE_Reference_Handler(details=["Id", "Title", "Tags"])
    parser.setContentHandler(Handler)
    parser.parse("Posts.xml")
