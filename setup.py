# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="kovot-mastodon",
    version="0.1.0",
    description="Kovot stream for Mastodon",
    license="MIT",
    author="Kazuhiro Hishinuma",
    packages=find_packages(),
    install_requires=[
        "git+https://github.com/kenkov/kovot@0.2.4",
        "Mastodon.py>=1.3.1",
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ]
)
