#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-pagseguro',
    version="beta",
    author='Fabio Cerqueira',
    maintainer="Bruno Gola",
    maintainer_email="brunogoal@gmail.com",
    url='http://github.com/fabiocerqueira/django-pagseguro',
    install_requires=[
        'Django>=1.0'
    ],
    description = 'A pluggable Django application for integrating PagSeguro payment system',
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
