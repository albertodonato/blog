AUTHOR = 'Alberto Donato'
SITENAME = "Ack's blog"
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

# Links section
LINKS = ()

# Social links
SOCIAL = (
    ('google+', 'https://plus.google.com/104904437381999058439/'),
    ('bitbucket', 'https://bitbucket.org/ack'),
    ('launchpad', 'https://launchpad.net/~ack'),
    ('rss', SITEURL + '/' + FEED_ALL_ATOM))

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

DEFAULT_PAGINATION = 5

DEFAULT_CATEGORY = 'misc'

TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = [
    'images', 'files', 'extra/robots.txt', 'extra/custom.css']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/favicon.ico': {'path': 'static/favicon.ico'}}

THEME = '../pelican-themes/pelican-bootstrap3'

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = ['tipue_search']

PYGMENTS_STYLE = 'default'
# PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

#
# pelican-bootstrap3 theme-specific settings
#

BOOTSTRAP_THEME = 'cerulean'

BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True

SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = True

DISPLAY_BREADCRUMBS = False

CC_LICENSE = "CC-BY-NC-SA"

CUSTOM_CSS = 'static/custom.css'


#
# plugin configurations
#
