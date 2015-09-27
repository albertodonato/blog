import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://albertodonato.net/blog'
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

#
# theme-specific settings
#
LOCAL_RESOURCES = False
FAVICON_URL = 'https://albertodonato.net/favicon.png'
GOOGLE_ANALYTICS = 'UA-64608830-1'
