.. _crawler:

Django Crawler
===============

The code
--------

You can find the code on github: http://github.com/ericholscher/django-crawler

Core features
-------------

The Crawler at the beginning loops through all of your URLConfs. It
then loads up all of the regular expressions from these URLConfs to
examine later. Once the crawler is done crawling your site, it will
tell you what URLConf entries are not being hit.

Plugins
-------

The main functionality of Crawler is implemented through plugins.

.. toctree::
    :maxdepth: 2

    plugins/index


Usage
~~~~~

The crawler is implemented as a management command.

Step 1: `pip install django-crawler`

Step 2: Add `crawler` to your `INSTALLED_APPS`

Step 3: The syntax for invoking the crawler looks like:

.. sourcecode:: python

     ./manage.py crawler [options] [relative_start_url]

Relative start URLs are assumed to be relative to the site root and should
look like 'some/path', 'home', or even '/'. The relative start URL will be
normalized with leading and trailing slashes if they are not provided. The
default relative start URL is '/'.

The crawler at the moment has 4 options implemented on it. It crawls your
site using the `Django Test Client
<http://docs.djangoproject.com/en/dev/topics/testing/#module-
django.test.client>`__ (so no network traffic is required!) This
allows the crawler to have intimate knowledge of your Django Code.
This allows it to have features that other crawlers can't have.


Options
~~~~~~~

-v --verbosity [0,1,2]
~~~~~~~~~~~~~~~~~~~~~~

Same as most django apps. Set it to 2 to get a lot of output. 1 is the
default, which will only output errors.

