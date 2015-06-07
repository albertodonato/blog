#!/usr/bin/env python

AUTHOR = 'Alberto Donato'
SITENAME = 'Significant white space'
SITEURL = 'http://localhost:8000'

RELATIVE_URLS = True

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'

# URL formats
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_URL = 'category/{slug}.html'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('launchpad', 'https://launchpad.net/~ack'),
    ('bitbucket', 'https://bitbucket.org/ack'),
    ('google+', 'https://plus.google.com/104904437381999058439'),
    ('linkedin', 'https://it.linkedin.com/in/albertodonato'),
    ('rss', SITEURL + '/' + FEED_ALL_ATOM))

DEFAULT_PAGINATION = 5

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_TAGS_ON_SIDEBAR = True

CC_LICENSE = "CC-BY-NC-SA"


STATIC_PATHS = [
    'static/extra', 'static/files', 'static/images', 'static/custom.css']

EXTRA_PATH_METADATA = {
    'static/extra/favicon.ico': {'path': 'favicon.ico'}}


THEME = '../pelican-bootstrap3'

PLUGIN_PATHS = ['../pelican-plugins']

# PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#            'liquid_tags.youtube', 'liquid_tags.vimeo',
#            'liquid_tags.include_code', 'liquid_tags.notebook']


BOOTSTRAP_THEME = 'cerulean'

BOOTSTRAP_NAVBAR_INVERSE = True

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True

DISPLAY_BREADCRUMBS = True

PYGMENTS_STYLE = 'default'
# PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

CUSTOM_CSS = 'static/custom.css'

# ABOUT_ME = 'Alberto Donato'
