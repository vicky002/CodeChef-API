#coding=utf-8

from bs4 import BeautifulSoup
from codechef import try_cast_int
import feedparser
import re
import requests
import string

### Configuration ###

POSSIBLE_FEED_KEYS = ['short', 'long', 'contest', 'summary', 'details']

### Enumerated Types ###
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value,key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum',(),enums)

