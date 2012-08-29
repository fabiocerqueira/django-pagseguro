#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

setup(
    name='django-pagseguro',
    version="1.2.2",
    author='Fábio Cerqueira',
    author_email='cerqueirasfabio@gmail.com',
    maintainer="Fábio Cerqueira",
    maintainer_email="cerqueirasfabio@gmail.com",
    url='http://github.com/fabiocerqueira/django-pagseguro',
    install_requires=[
        'Django>=1.0'
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
