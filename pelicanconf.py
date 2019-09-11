import pelican

AUTHOR = 'Alberto Donato'
SITENAME = 'Significant white space'
SITEURL = 'http://localhost:8000'

RELATIVE_URLS = True

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# URL formats
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'
CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = 'categories.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_URL = 'archives/{date:%Y}/index'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_URL = 'archives/{date:%Y}/{date:%m}/index'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_URL = 'archives/{date:%Y}/{date:%m}/{date:%d}/index'
DAY_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/{date:%d}/index.html'

# Links section
LINKS = ()

# Social links
SOCIAL = (
    ('github', 'https://github.com/albertodonato'),
    ('linkedin', 'https://www.linkedin.com/in/albertodonato'),
    ('twitter', 'https://twitter.com/AlbDnt'),
)

DIRECT_TEMPLATES = (
    'index', 'categories', 'tags', 'authors', 'archives', 'search')

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'

STATIC_PATHS = ['images', 'files', 'extra/robots.txt']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}}

THEME = '../pelican-chemistry'

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = ['headerid.headerid', 'tipue_search', 'sitemap']

#
# theme-specific settings
#

# Export pelican version to theme
PELICAN_VERSION = pelican.__version__

TAGLINE = 'this is where my brain dumps stuff'

LICENSE_NAME = 'CC BY-SA 4.0'
LICENSE_URL = 'https://creativecommons.org/licenses/by-sa/4.0/'

PAGES_ON_MENU = True
INDEXES_ON_MENU = True

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

#
# plugin: headerid
#
HEADERID_LINK_CHAR = '¶'
