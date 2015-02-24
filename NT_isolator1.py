"""
Automate the extraction step. This should be followed by NT_isolator2.py.
The reason they are done separately is because python's sax module does
fancy threading and asynchronous computation, and I don't know anything
about threading. So this is currently run in bash with bash's wait called
between the two.

To generalize, this should accept command-line arguments. Not important.
"""

import xml.sax
import reference_isolator


def main():
    """
    Extract `reference-request` tags from `Posts.xml` and output xml in
    `ref_reqs.xml`
    """
    print '(>")> Beginning extraction of reference-requests from Posts.xml.'
    parser = xml.sax.make_parser()
    RefReqIsolator = reference_isolator.MSE_Reference_Isolator(output_file="ref_reqs.xml")
    parser.setContentHandler(RefReqIsolator)
    parser.parse("Posts.xml")
    print '(>")> Reference Requests extracted from Posts.xml.'

if __name__ == "__main__":
    main()
