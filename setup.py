#!/usr/bin/env python

import json
from setuptools import setup


def get_version():
    with open('package.json', 'r') as f:
        package = json.load(f)
        return(package['dependencies']['@octokit/routes'])


setup(
    name='octokitpy-routes',
    version=get_version(),
    description='Routes for octokitpy',
    long_description='Routes from the NPM published octokit routes',
    author='Kyle Hornberg',
    author_email='kyle.hornberg@gmail.com',
    url='https://github.com/khornberg/routes',
    packages=['routes'],
)
