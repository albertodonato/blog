#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Alberto Donato'
SITENAME = u'Significant white space'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Launchpad', 'https://launchpad.net/~ack'),
    ('BitBucket', 'https://bitbucket.org/ack'))

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = '../pelican-bootstrap3'

# pelican-bootstrap3 settings

BOOTSTRAP_THEME = 'spacelab'  # united cerulean slate spacelab

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True

PYGMENTS_STYLE = 'default'
# PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

# CUSTOM_CSS = 'static/custom.css'

ABOUT_ME = "Alberto Donato"
