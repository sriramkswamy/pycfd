# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pycfd',
    version='0.0.0',
    description='Python package for some CFD functions',
    long_description=readme,
    author='Sriram Krishnaswamy',
    author_email='sriramkswamy@outlook.com',
    url='https://github.com/sriramkswamy/pycfd',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
