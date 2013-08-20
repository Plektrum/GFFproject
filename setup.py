'''
@author: Plektrum
'''
#setup py
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='GffReader',
    version='1.0',
    scripts=['GffReader.py']
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
