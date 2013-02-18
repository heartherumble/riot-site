Riot Inc. Website
=================
This the source repository for the Riot Inc. website. The actual site is
served from the ``gh-pages`` branch.

3rd Party Requirements
----------------------
* Markdown==2.2.0
* Pygments==1.5
* pelican==3.0

Initial Setup
-------------
From a ``BASE_DIR`` (e.g. ``/dev/riot/``) do the following:

* Create a ``src`` folder and ``gh-pages`` folder
* Create a virtualenv and activate it
* Checkout the ``master`` branch
* Checkout the ``gh-pages`` branch
* Install requirements

```bash
$ mkdir -p src gh-pages
$ virtualenv ve
$ source ve/bin/activate
$ cd src && git clone git@github.com:heartherumble/riot-site.git
$ git checkout master
$ cd ../gh-pages/ && git clone git@github.com:heartherumble/riot-site.git
$ git checkout gh-pages
$ cd ../ && pip install -r src/requirements.txt
```

To preview the site locally:

```bash
$ cd BASE_DIR/src/riot-site/
$ ./develop_server.sh start
```

This rebuilds the site to ``BASE_DIR/gh-pages`` and does so automatically when
you create or edit content.

To stop the server:

```bash
$ ./develop_server.sh stop
```

> **NOTE** :
> Contrary to the pelican docs, we are not going to use the Makefile or
> the make command.

Command-line Utility
--------------------
```bash
$ ./pelican_new_post.py --help
usage: pelican_new_post.py [-h] [--page] [--post] [-c CATEGORY] [-t TAGS] title

Create a new post or page in Pelican, if post or page is unspecified, it will
create a post by default

positional arguments:
  title        Post/Page title, enclosed in quotes

optional arguments:
  -h, --help   show this help message and exit
  --page       Create a new page
  --post       Create a new blog post
  -c CATEGORY  Category for post/page
  -t TAGS      Tags, comma separated
```

The command can be found at this path:
``BASE_DIR/src/riot-site/``

Make sure your virtualenv is active before using this utility.

How-to: Author & publish a blog post
-------------------------------------
From the command line:

```bash
$ ./pelican_new_post.py -c category1,category2 -t tag1,tag2 "My new blog post"
```

> **NOTE** :
> Categories and tags are optional.

Your new post with the appropriate meta info can be found at:
``BASE_DIR/src/riot-site/content/``

Edit the file with your content and commit the result. If you have the development
server running, it will have already compiled it and updated the ``gh-pages``
folder. You can then also preview this post on your local machine at
``http://localhost:8000/``

To deploy, switch to ``BASE_DIR/gh-pages``, commit the changes and push up to
Github.


How-to: Author & publish a new page
-----------------------------------
From the command line:

```bash
$ ./pelican_new_post.py -c category1,category2 -t tag1,tag2 --page "My new page"
```

> **NOTE** :
> Categories and tags are optional.

Your new page with the appropriate meta info can be found at:
``BASE_DIR/src/riot-site/content/pages/``

Edit the file with your content and commit the result. If you have the development
server running, it will have already compiled it and updated the ``gh-pages``
folder. You can then also preview this page on your local machine at
``http://localhost:8000/``

To deploy, switch to ``BASE_DIR/gh-pages``, commit the changes and push up to
Github.

How-to: Edit the homepage
-------------------------
The homepage is not in Markdown. You can edit the content by editing this file:
``BASE_DIR/src/riot-site/themes/templates/pages/index.html``.

The header and footer content are includes:
* ``BASE_DIR/src/riot-site/themes/riot-theme/templates/pages/footer.html``
* ``BASE_DIR/src/riot-site/themes/riot-theme/templates/pages/header.html``
