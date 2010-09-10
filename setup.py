from distutils.core import setup

setup(
    name = "django-crawler",
    version = "0.1",
    packages = [
        "crawler",
        "crawler.management",
        "crawler.management.commands",
        "crawler.plugins",
    ],
    author = "Eric Holscher, Chris Adams",
    author_email = "eric@ericholscher.com",
    description = "A crawler using the Django Test Client",
    url = "http://github.com/ericholscher/django-crawler/tree/master",
)
