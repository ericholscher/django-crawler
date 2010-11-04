.. _crawler:

Django Crawler
===============

The code
--------

You can find the code on github: http://github.com/ericholscher/django-crawler

The mailing list for the project is on Google Groups: http://groups.google.com/group/django-testing



Usage
~~~~~

The crawler is implemented as a management command.

Step 1: `pip install -e git://github.com/ericholscher/django-crawler#egg=crawler`

Step 2: Add `crawler` to your `INSTALLED_APPS`

Step 3: The syntax for invoking the crawler looks like:

.. sourcecode:: python

     ./manage.py crawl [options] [relative_start_url]


.. note::

    Running a simple `./manage.py crawl` will work.

Relative start URLs are assumed to be relative to the site root and should
look like 'some/path', 'home', or even '/'. The relative start URL will be
normalized with leading and trailing slashes if they are not provided. The
default relative start URL is '/'.

The crawler crawls your site using the `Django Test Client
<http://docs.djangoproject.com/en/dev/topics/testing/#module-
django.test.client>`__ (so no network traffic is required!) This
allows the crawler to have intimate knowledge of your Django Code.
This allows it to have features that other crawlers can't have.

Plugins
-------

The main functionality of Crawler is implemented through plugins.

.. toctree::
    :maxdepth: 2

    plugins/index



Global Options
--------------

-v --verbosity [0,1,2,3]
~~~~~~~~~~~~~~~~~~~~~~

Same as most django apps. Set it to 2 to get a lot of output. 1 is the
default, which will only output errors.

Setting output to 3 will show possibly really verbose debug output. This
includes links that go over the depth allowed, and external links in your HTML.

