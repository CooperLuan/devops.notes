#!/bin/bash
if [ ! -f bin/python ]; then
    virtualenv -p /usr/bin/python3 .
fi
bin/pip install -r requirements.txt -i http://pypi.douban.com/simple
