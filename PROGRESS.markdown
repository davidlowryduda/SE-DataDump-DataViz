
I want to be able to easily and quickly manipulate SE data through the xml data dumps using a variety of python tools.
So I am building some of these tools here. Closely associated with this goal is the goal of beautiful presentation
of the data found from these tools.

Reference-Request Project
=========================

  Here's an idea. Let's answer the question *How much overlap is there in the reference-request question on the site?*
  To begin, let's try to understand overlap in the number theory tags.

  Right now, we have <./reference_isolator.py>, which will narrow down the POSTS.xml to just those questions with certain
  tags (actually, questions with tags containing certain strings). It outputs a (much much smaller) xml file.

  There is also <./NT_isolator.py>, which further narrows down the xml file to just those with number theory tags.

  Ideas
  -----

  Visualize how often the same references are given.
  1. Extract the PostId's from NT_ref_reqs.xml
  2. Then pull out the relevant posts from POSTS.xml
    - This could be done data-structurally, and ideally outputting another xml file with proper heirarchy.
    - A dictionary with {PostID: [Question, [Answers]]} would be a good and relatively easy intermediate step
    - Then XMLGenerator can take in (question/answer, attributes) to make the correct heirarchy
    - Alternatively, this isn't actually necessary. If the relevant posts and questions are in the same page,
      creating the data won't be hard.
  3. By far the hardest part will be identifying which references are mentioned in many posts. Perhaps Joanna knows
     how to suggestively isolate names of references. Barring that, noting which ones appear as links is a good start.
  4. Make a graph with the various references at the "hubs" and the posts at the wheels. If the questions interlink,
     they can be connected too.
  5. Visualize this graph with d3.

  Extra points:
  6. Incorporate comments
  7. Associate references with users who give those references. Which reference does the same user give the most often?





vim: foldmethod=indent foldcolumn=2 ts=2 sw=2 sts=2
