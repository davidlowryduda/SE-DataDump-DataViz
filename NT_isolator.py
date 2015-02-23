#!/usr/bin/env python
# encoding: utf-8

import xml.sax
import reference_isolator

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    Handler = reference_isolator.MSE_Reference_Isolator(wordlist=["number-theory"],
                                                        output_file="NT_ref_reqs.xml")
    parser.setContentHandler(Handler)
    parser.parse("ref_reqs.xml")
    print '(>")> Process Completed'
