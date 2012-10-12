Date: 2011-02-19
Title: Backing up servers to S3
Tags: aws, s3, backups
Slug: backing-up-servers-to-s3

As part of our build automation here at Riot, we've been trying to find solid options to backup our servers (configs, logs, data etc.) to an off-site location. Our provider does daily backups of our servers and restores data on demand, which is certainly nice, but left us wanting more fine grained control of the process. Cost, simplicity and security were our top concerns, and our search led us to start using [duplicity](http://www.nongnu.org/duplicity/) combined with Amazon's [S3](https://s3.amazonaws.com/). Here's how we use it.

Setup
-----
You will need to have librsync installed on your system as well. In ubuntu: 
    
    apt-get install librsync-dev

Since duplicity is a python app, we chose to install it in a virtualenv. It's pip installable, but is not in pypi, so you will have to point pip at the tarball.

    virtualenv duplicity
    cd duplicity
    source bin/activate
    pip install -E . http://code.launchpad.net/duplicity/0.6-series/0.6.11/+download/duplicity-0.6.11.tar.gz boto

_or_ in ubuntu:
    
    apt-get install duplicity

If you want to encrypt your backups you will need to generate a GnuPG key, like so:
    
    gpg --gen-key

You can accept the default options during install, make sure you add in a passphrase to the key, as duplicity will not work without it.

Backup
----------
S3 is just one of the many backends duplicity supports. Their [docs](http://www.nongnu.org/duplicity/duplicity.1.html) have more info. 

Here's our backup script:

    export AWS_ACCESS_KEY_ID='xxxxxx'
    export AWS_SECRET_ACCESS_KEY='xxxxxx'
    export PASSPHRASE='xxxxxx'
    export NOW=`date +"%Y-%m-%d-%H-%M"`

    duplicity --exclude ".*" --include "**" --full-if-older-than 30D \
              --log-file /var/log/duplicity/s3-$NOW.log --verbosity 6 \
              --s3-use-rrs --s3-use-new-style --asynchronous-upload \
              /var/www/backups s3+http://riot.xxxx.xxxx

    export AWS_ACCESS_KEY_ID=
    export AWS_SECRET_ACCESS_KEY=
    export PASSPHRASE=
    export NOW=

Restore
-----------
Restoring is a snap too. Though we haven't had the need to restore yet, this is how you would:

    # Restore a file
    duplicity --file-to-restore var/www/backups/code.tar s3+http://riot.xxxx.xxxx ~/tmp/restore

    # Restore a directory
    duplicity --file-to-restore var/www/backups/db s3+http://riot.xxxx.xxxx ~/tmp/restore

    # Restore everything from a point in time
    duplicity -t 2011-02-19T12:20:45 s3+http://riot.xxxx.xxxx ~/tmp/restore

The backup script runs hourly and does incremental backups to our S3 bucket.
