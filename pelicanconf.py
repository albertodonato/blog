AUTHOR = 'Alberto Donato'
SITENAME = 'Significant white space'
SITEURL = 'http://localhost:8000'

RELATIVE_URLS = True

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# URL formats
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
CATEGORY_SAVE_URL = 'category/{slug}.html'

FEED_DOMAIN = SITEURL

# Links section
LINKS = ()

# Social links
SOCIAL = (
    ('bitbucket', 'https://bitbucket.org/ack'),
    ('launchpad', 'https://launchpad.net/~ack'),
    ('github', 'https://github.com/albertodonato'),
    ('google+', 'https://plus.google.com/104904437381999058439/'))

DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'authors', 'archives')

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'

STATIC_PATHS = ['images', 'files', 'extra/robots.txt']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}}

THEME = '../pelican-chemistry'

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = ['sitemap']

#
# theme-specific settings
#
TAGLINE = 'this is where my brain dumps stuff'

LICENSE_NAME = 'CC BY-SA 4.0'
LICENSE_URL = 'https://creativecommons.org/licenses/by-sa/4.0/'

DISPLAY_PAGES_ON_MENU = True
CATEGORIES_LINK_ON_MENU = True
TAGS_LINK_ON_MENU = True
ARCHIVES_LINK_ON_MENU = True

LOCAL_RESOURCES = True

#
# plugin: sitemap
#
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
