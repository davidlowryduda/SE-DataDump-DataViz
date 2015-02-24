#!/usr/bin/env python
# encoding: utf-8

import xml.sax
import os


class XML_Extractor(xml.sax.ContentHandler):
    """
    Takes in xml document and creates documents containing desired attribute
    fields of desired xml tags.
    """
    def __init__(self, output_dir="DATA", output_prefix="post",
                 attrs=["Title", "Tags", "Score", "Id", "ParentId", "Body"]):
        self.output_dir = output_dir
        self.output_prefix = output_prefix
        self.attrs = attrs
        self.num = 1
        return

    def startDocument(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def startElement(self, tag, attributes):
        """Activates on opening each row"""
        fname = self.output_dir + "/" + self.output_prefix + str(self.num) + ".txt"
        self.f = open(fname, "w")
        for data in self.attrs:
            if data in attributes:
                header = u"## " + data.encode('utf-8') + ":\n"
                self.f.write(header)
                self.f.write(attributes[data].encode('utf-8'))
                self.f.write("\n\n")

    def endElement(self, tag):
        """Activates on closing each row"""
        self.f.close()
        self.num += 1

    def endDocument(self):
        return

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    Handler = XML_Extractor()
    parser.setContentHandler(Handler)
    parser.parse("NT_ref_reqs.xml")
    print '(>")> Process Completed'
