#!/bin/bash

python ./NT_isolator1.py
wait
python ./NT_isolator2.py
wait
python ./NT_isolator3.py
echo '(>")> Script completed gracefully'
