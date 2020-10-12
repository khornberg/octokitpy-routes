#!/usr/bin/env python

from setuptools import setup


setup(
    name='octokitpy-routes',
    version='2.3.0',
    description='Routes for octokitpy',
    long_description='Routes from the NPM published octokit routes',
    author='Kyle Hornberg',
    author_email='kyle.hornberg@gmail.com',
    url='https://github.com/khornberg/octokitpy-routes',
    packages=['octokit_routes'],
    include_package_data=True,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ]
)
