"""
Automate the extraction step. This should be preceded by NT_isolator1.py
and followed by NT_isolator3.py.  The reason they are done separately is
because python's sax module does fancy threading and asynchronous computation,
and I don't know anything about threading. So this is currently run in bash
with bash's wait called between the two.

To generalize, this should accept command-line arguments. Not important.
"""

import xml.sax
import reference_isolator


def main():
    """
    Extract `wordlist` tags from `ref_reqs.xml` and output xml in
    `NT_ref_reqs.xml`
    """
    print '(>")> Beginning to extract just number theory requests.'
    parser = xml.sax.make_parser()
    Handler = reference_isolator.MSE_Reference_Isolator(wordlist=["number-theory"],
                                                        output_file="NT_ref_reqs.xml")
    parser.setContentHandler(Handler)
    parser.parse("ref_reqs.xml")
    print '(>")> Process Completed'

if __name__ == "__main__":
    main()
