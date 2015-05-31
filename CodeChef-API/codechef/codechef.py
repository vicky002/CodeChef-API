#coding=utf-8

from bs4 import BeautifulSoup
import re
import requests

#################################################
# Helpers
###############################################

def try_cast_int(s):
    try:
        pattern = re.compile(r'([0-9]+(\.[0-9]+)*[ ]*[Kk])|([0-9]+)')
        raw_result = re.search(pattern,s).groups()
        if raw_result[2] != None:
            return int(raw_result[2])
        elif raw_result[1] == None:
            raw_result = re.search(r'([0-9])+',raw_result[0])
            return int(raw_result.groups()[0]) * 1000
        else:
            raw_result = re.search(r'([0-9]+)\.([0-9]+)',raw_result[0]).groups()
            return int(raw_result[0]) * 1000 + int(raw_result[1]) * 100
    except:
        return s

