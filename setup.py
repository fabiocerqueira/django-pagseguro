#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-pagseguro',
    version="1.0",
    author='Fábio Cerqueira',
    author_email='cerqueirasfabio@gmail.com',
    maintainer="Fábio Cerqueira",
    maintainer_email="cerqueirasfabio@gmail.com",
    url='http://github.com/fabiocerqueira/django-pagseguro',
    install_requires=[
        'Django>=1.0'
    ],
    description = 'A pluggable Django application for integrating PagSeguro payment system',
    long_description=read('README.rst'),
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
