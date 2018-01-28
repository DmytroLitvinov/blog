#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.DmytroLitvinov.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
GOOGLE_ANALYTICS = 'UA-92540730-1'
GOOGLE_TAG_MANAGER = 'GTM-T2GHTH2'
DISQUS_SITENAME = "dmytrolitvinov-github-io"
ADD_THIS_ID = 'ra-58af06693081c196'