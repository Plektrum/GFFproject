'''
Created on 8 Jul 2013

@author: Plektrum
'''
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='GffReader',
    version=GffReader.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
