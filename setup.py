# -*- coding: utf-8 -*-
# Copyright 2014 John Vandenberg
# Licensed under the MIT License, see LICENSE file for details.

"""Sphinx "epytext" extension."""

from setuptools import setup, find_packages

setup(
    name='sphinx-epytext',
    version='0.0.3',
    url='https://github.com/jayvdb/sphinx-epytext',
    download_url='http://pypi.python.org/pypi/sphinx-epytext',
    license='MIT',
    author='John Vandenberg',
    author_email='jayvdb@gmail.com',
    description=__doc__,
    long_description=open('README.rst', 'r').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    install_requires=['sphinx>=0.4'],
)
