"""
Automate the extraction step. This should be preceded by NT_isolator1.py and
NT_isolator2.py.  The reason they are done separately is because python's sax
module does fancy threading and asynchronous computation, and I don't know
anything about threading. So this is currently run in bash with bash's wait
called between the two.

To generalize, this should accept command-line arguments. Not important.
"""

import xml.sax
import text_extractor


def main():
    """
    Extract the text from posts in NT_ref_reqs.xml to the DATA/
    directory.
    """
    print '(>")> Beginning extraction of text from NT_ref_reqs.xml'
    parser = xml.sax.make_parser()
    Handler = text_extractor.XML_Extractor()
    parser.setContentHandler(Handler)
    parser.parse("NT_ref_reqs.xml")
    print '(>")> Text extracted. The data is not in DATA/'

if __name__ == "__main__":
    main()
