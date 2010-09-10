.. _time:

Time Plugin
-----------


This plugin will measure the time that it took to run each of your views, and
output the ones that have taken the longest.

Available options
~~~~~~~~~~~~~~~~~

-t --time
`````````

The `-t` option, as the help says: Pass -t to time your requests. This
outputs the time it takes to run each request on your site. This
option also tells the crawler to output the top 10 URLs that took the
most time at the end of it's run. Here is an example output from
running it on my site with `-t -v 2`:

.. sourcecode:: python

    Getting /blog/2007/oct/17/umw-blog-ring/ ({}) from (/blog/2007/oct/17/umw-blog-ring/)
    Time Elapsed: 0.256254911423
    Getting /blog/2007/dec/20/logo-lovers/ ({}) from (/blog/2007/dec/20/logo-lovers/)
    Time Elapsed: 0.06906914711
    Getting /blog/2007/dec/18/getting-real/ ({}) from (/blog/2007/dec/18/getting-real/)
    Time Elapsed: 0.211296081543
    Getting /blog/ ({u'page': u'5'}) from (/blog/?page=4)
    Time Elapsed: 0.165636062622
    NOT MATCHED: account/email/
    NOT MATCHED: account/register/
    NOT MATCHED: admin/doc/bookmarklets/
    NOT MATCHED: admin/doc/tags/
    NOT MATCHED: admin/(.*)
    NOT MATCHED: admin/doc/views/
    NOT MATCHED: account/signin/complete/
    NOT MATCHED: account/password/
    NOT MATCHED: resume/
    /blog/2008/feb/9/another-neat-ad/ took 0.743204
    /blog/2007/dec/20/browser-tabs/#comments took 0.637164
    /blog/2008/nov/1/blog-post-day-keeps-doctor-away/ took 0.522269
