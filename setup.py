#!/usr/bin/env python
from setuptools import setup
import os

README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_requirements(filename='requirements.txt'):
    ret = []
    if os.path.isfile(filename):
        for x in open(filename):
            ret.append(x.strip())
    return ret


def get_version(dir_name):
    for x in open(os.path.join(dir_name, '__init__.py')):
        x = [y.strip() for y in x.split('=')]
        if len(x) == 2 and x[0] == '__version__':
            return eval(x[1])
    raise '__version__ not found in __init__.py'


setup(
    name="twitterss",
    version=get_version('twitterss'),
    packages=["twitterss"],
    include_package_data=True,
    description="Get twitter as RSS feeds.",
    long_description=README,
    author="Julien Collas",
    author_email="jul.collas@gmail.com",
    install_requires=get_requirements(),
)
