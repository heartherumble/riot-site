#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Riot"
SITENAME = u"Riot Inc."
SITEURL = 'http://riot.io'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True
THEME = 'riot-theme'
PAGE_DIR = 'pages'

DELETE_OUTPUT_DIRECTORY = False
ARTICLE_URL = 'notebook/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'notebook/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
