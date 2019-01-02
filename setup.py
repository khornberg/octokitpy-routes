#!/usr/bin/env python

from setuptools import setup


setup(
    name='octokitpy-routes',
    version='0.0.5',
    description='Routes for octokitpy',
    long_description='Routes from the NPM published octokit routes',
    author='Kyle Hornberg',
    author_email='kyle.hornberg@gmail.com',
    url='https://github.com/khornberg/routes',
    packages=['routes'],
    include_package_data=True,
)
