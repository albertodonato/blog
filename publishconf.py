import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

DELETE_OUTPUT_DIRECTORY = True

DOMAIN = 'https://albertodonato.net/'

SITEURL = DOMAIN + 'blog'
FEED_DOMAIN = SITEURL

RELATIVE_URLS = False

#
# theme-specific settings
#
SEARCH_URL = 'search'

LOCAL_RESOURCES = False

FAVICON_URL = DOMAIN + 'favicon.png'
GOOGLE_ANALYTICS = 'UA-64608830-1'
