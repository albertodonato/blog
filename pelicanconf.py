AUTHOR = 'Alberto Donato'
SITENAME = 'Significant white space'
SITEURL = 'http://localhost:8000'

RELATIVE_URLS = True

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# URL formats
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

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

DEFAULT_CATEGORY = 'misc'

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_TAGS_ON_SIDEBAR = True

CC_LICENSE = "CC-BY-NC-SA"

STATIC_PATHS = [
    'images', 'files', 'extra/robots.txt', 'extra/custom.css']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/favicon.ico': {'path': 'static/favicon.ico'}}


THEME = '../pelican-bootstrap3'

PLUGIN_PATHS = ['../pelican-plugins']

# PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#            'liquid_tags.youtube', 'liquid_tags.vimeo',
#            'liquid_tags.include_code', 'liquid_tags.notebook']


BOOTSTRAP_THEME = 'cerulean'

BOOTSTRAP_NAVBAR_INVERSE = True

SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = True

DISPLAY_BREADCRUMBS = True

PYGMENTS_STYLE = 'default'
# PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

CUSTOM_CSS = 'static/custom.css'
