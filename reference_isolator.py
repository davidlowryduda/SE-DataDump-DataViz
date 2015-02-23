#!/usr/bin/env python
# encoding: utf-8

import xml.sax
import xml.sax.saxutils


class MSE_Reference_Isolator(xml.sax.ContentHandler):
    """
    Takes in MSE data dump and returns xml file `output_file` containing only
    those rows with tags containing `wordlist`.
    """
    def __init__(self, wordlist=["reference", "book", "learning"],
                 output_file="output.xml"):
        self.details = details
        self.output_file = file(output_file, "wb")
        self.wordlist = wordlist
        self.in_element = False
        self.logger = xml.sax.saxutils.XMLGenerator(self.output_file, "utf-8")
        self.logger.startDocument()
        return

    def startElement(self, tag, attributes):
        """Activates on opening each row"""
        if (attributes.has_key("Tags")) and (self.has_keywords(attributes["Tags"])):
            self.in_element = True
            self.logger.startElement(tag, attributes)

    def endElement(self, tag):
        """Actives on closing each row"""
        if self.in_element:
            self.logger.endElement(tag)
            self.in_element = False
            self.output_file.write("\n")

    def has_keywords(self, body):
        """Returns if body contains any of self.wordlist"""
        for word in self.wordlist:
            if word in body:
                return True
        return False

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    Handler = MSE_Reference_Handler(output_file="ref_reqs.xml")
    parser.setContentHandler(Handler)
    parser.parse("Posts.xml")
    print '(>")> Process Completed'
