#!/usr/bin/env python

import argparse
import datetime
import os
import sys

from pelican.utils import slugify

try:
    import pelican
except ImportError:
    sys.stderr.write(u'Cannot import Pelican, please install it \n')
    sys.exit(0)

PELICAN_ROOT = os.path.dirname(os.path.abspath(__file__))


def create_file(docroot, filename, date_string, title, *args, **kwargs):
    path = os.path.join(docroot, filename)
    new_file = open(path, 'w')
    new_file.write('Date: {0}\n'.format(date_string))
    new_file.write('Title: {0}\n'.format(title))
    new_file.write('Slug: {0}\n'.format(slugify(title)))
    if kwargs.get('tags'):
        new_file.write('Tags: {0}\n'.format(kwargs.get('tags')))
    if kwargs.get('category'):
        new_file.write('Category: {0}\n'.format(kwargs.get('category')))
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Create a new post or page in Pelican, if post or page is \
        unspecified, it will create a post by default",
        add_help=True)

    parser.add_argument('--page', action="store_true", default=False,
                        help="Create a new page")
    parser.add_argument('--post', action="store_true", default=False,
                        help="Create a new blog post")
    parser.add_argument('-c', action="store", dest='category',
                        help="Category for post/page")
    parser.add_argument('-t', action="store", dest='tags',
                        help="Tags, comma separated")
    parser.add_argument('title', action="store",
                        help="Post/Page title, enclosed in quotes")

    args = parser.parse_args()

    # Check if new content is page or post
    # Construct correct path (from settings)
    if args.page:
        docroot = os.path.join(PELICAN_ROOT, 'content/pages')
        ctype = 'page'
    else:
        docroot = os.path.join(PELICAN_ROOT, 'content')
        ctype = 'post'

    # Check if path to content or pages exists
    if not os.path.exists(docroot):
        sys.stderr.write(u'You have not installed Pelican properly,\
            please re-install')
        sys.exit(0)

    # Get title from args
    # slugify title
    title = args.title
    slug = slugify(title)

    # Get tags and category from args (optional)
    tags = args.tags
    category = args.category

    # contruct file name
    date_string = datetime.datetime.now().strftime('%Y-%m-%d')
    filename ='{0}-{1}.{2}'.format(date_string, slug, 'md')
    success = False
    if os.path.exists(os.path.join(docroot, filename)):
        response = raw_input('{0} already exists. Do you want to overwrite? (y/n)'.format(filename))
        if response == 'y' or response == 'Y':
            sys.stdout.write(u'\nOverwriting {0}: {1}'.format(ctype, filename))
            success = create_file(docroot, filename, date_string, title,
                        tags=tags, category=category)
        elif response == 'n' or response == 'N':
            sys.stdout.write(u'\nAborting...\n')
            sys.exit(0)
        else:
            sys.stdout.write(u'\nInvalid response. Please retry.')
    else:
        sys.stdout.write(u'\nCreating new {0}: {1}'.format(ctype, filename))
        success = create_file(docroot, filename, date_string, title,
                    tags=tags, category=category)

    if success:
        sys.stdout.write(u'\n{0} created!\n'.format(ctype))
        sys.exit(0)
    else:
        sys.stdout.write(u'\nThere was a problem creating your {0}.\n'.format(ctype))
        sys.exit(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
