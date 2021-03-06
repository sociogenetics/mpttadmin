# -*- coding: utf-8 -*-
__author__ = 'tahy'

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mpttadmin',
    version='0.1.0',
    description='',
    long_description=read('README.md'),
    author='Potapov Pavel (tahy)',
    author_email='info@sociogenetics.ru',
    url='',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
