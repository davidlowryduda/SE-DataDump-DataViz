#!/usr/bin/env python
# encoding: utf-8
"""
##Posts
- `Id`
- `PostTypeId`
 1. Question
 2. Answer
 3. Orphaned tag wiki
 4. Tag wiki excerpt
 5. Tag wiki
 6. Moderator nomination
 7. "Wiki placeholder" (seems to only be the [election description](http://stackoverflow.com/posts/8041931/body))
 8. Privilege wiki
- `AcceptedAnswerId` (only present if PostTypeId is 1)
- `ParentID` (only present if PostTypeId is 2)
- `CreationDate`
- `Score`
- `ViewCount`
- `Body`
- `OwnerUserId` (present only if user has not been deleted; always -1 for tag wiki entries (i.e., the community user owns them))
- `OwnerDisplayName`
- `LastEditorUserId`
- `LastEditorDisplayName`="Rich B"
- `LastEditDate`="2009-03-05T22:28:34.823" - the date and time of the most recent edit to the post
- `LastActivityDate`="2009-03-11T12:51:01.480" - the date and time of the most recent activity on the post. For a question, this could be the post being edited, a new answer was posted, a bounty was started, etc.
- `Title`
- `Tags`
- `AnswerCount`
- `CommentCount`
- `FavoriteCount`
- `ClosedDate` (present only if the post is closed)
- `CommunityOwnedDate` (present only if post is community wikied)
"""
import xml.sax

ATTRIBUTES = ["Id",
              "PostTypeId",
              #"AcceptedAnswerId",
              #"ParentID",
              "CreationDate",
              "Score",
              "ViewCount",
              "Body",
              #"OwnerUserId",
              #"OwnerDisplayName",
              #"LastEditorUserId",
              #"LastEditorDisplayName",
              #"LastEditDate",
              #"LastActivityDate",
              "Title",
              "Tags",
              #"AnswerCount",
              #"CommentCount",
              #"FavoriteCount",
              #"ClosedDate",
              #"CommunityOwnedDate",
              ]
FILE = "Posts.xml"


class MSEHandler(xml.sax.ContentHandler):
    def __init__(self, details=[], func=None):
        self.CurrentData = ""
        self.details = details
        self.func = func

    def startElement(self, tag, attributes):
        """Retrieves the information from ATTRIBUTES constant above"""
        self.CurrentData = tag
        for item in self.details:
            if item in attributes:
                if not self.func:
                    print item + ":", attributes[item]
                else:
                    self.func(attributes[item])

    def endElement(self, tag):
        """thing"""
        self.CurrentData = ""


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    Handler = MSEHandler(details=ATTRIBUTES)
    parser.setContentHandler(Handler)
    parser.parse(FILE)
