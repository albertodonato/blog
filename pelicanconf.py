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
# TAG_URL = 'tag/{slug}.html'
# TAG_SAVE_AS = 'tag/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
CATEGORY_SAVE_URL = 'category/{slug}.html'

FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.rss.xml'

# Links section
LINKS = ()

# Social links
SOCIAL = (
    ('bitbucket', 'https://bitbucket.org/ack'),
    ('launchpad', 'https://launchpad.net/~ack'),
    ('github', 'https://github.com/theack'),
    ('google+', 'https://plus.google.com/104904437381999058439/'))

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')


DEFAULT_CATEGORY = 'misc'

STATIC_PATHS = [
    'images', 'files', 'extra/robots.txt', 'extra/custom.css']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/favicon.ico': {'path': 'static/favicon.ico'}}

THEME = '../pelican-alchemy/alchemy'

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = ['sitemap']

#
# theme-specific settings
#

SITE_SUBTEXT = 'this is where my brain dumps stuff'

LICENSE_NAME = 'CC BY-SA 4.0'
LICENSE_URL = 'https://creativecommons.org/licenses/by-sa/4.0/'

PAGES_ON_MENU = True
CATEGORIES_ON_MENU = True
TAGS_ON_MENU = True
ARCHIVES_ON_MENU = True

#
# plugin configs
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
