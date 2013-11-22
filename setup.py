#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='django-pagseguro',
    version="1.4.2",
    author='Fábio Cerqueira',
    author_email='cerqueirasfabio@gmail.com',
    maintainer="Fábio Cerqueira",
    maintainer_email="cerqueirasfabio@gmail.com",
    url='http://github.com/fabiocerqueira/django-pagseguro',
    install_requires=[
        'Django>=1.1'
    ],
    description = 'A pluggable Django application for integrating PagSeguro payment system',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
