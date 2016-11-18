#!/usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()



setup(name='python_people_names',
      version='0.0.1',
      description='people\'s name parser',
      author='lynzt',
      url='https://github.com/lynzt/python_people_names'
     )
