#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import datetime

AUTHOR = 'Dmytro Litvinov'
SITENAME = 'DevBlog with love'
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'Full Stack Python developer'
SITEDESCRIPTION = '{}\'s Thoughts and Writings'.format(AUTHOR)
SITELOGO = '//github.com/DmytroLitvinov.png'
FAVICON = '/images/favicon.png'
BROWSER_COLOR = '#9cb2ce'
PYGMENTS_STYLE = 'paraiso-dark'

THEME = 'Flex'
PATH = 'content'

DISABLE_URL_HASH = True

TIMEZONE = 'Europe/Kiev'
LOCALE = 'uk_UA'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

# Menu items
MENUITEMS = (('Archives', '/archives'),
             ('Categories', '/categories'),
             ('Tags', '/tags'),)

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'post_stats']

# URL settings(http://docs.getpelican.com/en/stable/settings.html#url-settings)
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

DEFAULT_CATEGORY = 'Dev'

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/DmytroLitvinov/'),
          ('twitter', 'https://twitter.com/DmytroLitvinov'),
          ('github', 'https://github.com/DmytroLitvinov'),
          ('gitlab', 'https://gitlab.com/DmytroLitvinov'))

DEFAULT_PAGINATION = 6

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'}
}

CUSTOM_CSS = 'static/custom.css'

# Creative Commons Licensing
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.date.today().year

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
