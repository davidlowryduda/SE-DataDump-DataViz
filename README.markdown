NT Branch
=========

For machine-learning purposes, the relevant data is located in the DATA/
directory. This represents only a very small proportion of the overall data.
Right now, it contains the questions posted under the tags reference-request
and number-theory on Math.SE.

The files follow a very simple set of rules. There are four classes of data
in each:

1. Title
2. Tags
3. Score
4. Body

Within the documents, the classes of data are separated from the data by pounds,
colons, and newlines. An example start is:

```
## Title:
<the title>

## Tags:
<the tags>

...
```

Look at any of the files for more examples. Note that the body contains the html
as it would appear on Math.SE. This means it includes tags, newlines, and some
metadata of its own. Notably, it contains urls, which is likely somewhat
distinguished data.

Legal
=====

This project and its source code is released under the GNU General Public
License as published by the Free Software Foundation, either version 3 of
the License, or (at your discretion) any later version. The license can
be found in the included LICENSE file.

For questions concerning the copyright or how to obtain copies of this project
or its contents under different licenses, contact the copyright holder
David Lowry-Duda (davidlowryduda@davidlowryduda.com)

The xml files here contain data from the [StackExchange Data
Dumps](http://blog.stackexchange.com/category/cc-wiki-dump/), and are therefore
licensed under [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/).

Copyright (C) 2015, David Lowry-Duda
All rights reserved.
