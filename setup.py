#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    'pytest',
]

setup(
    name='geotext',
    version='0.1.0',
    description='Geotext extracts country and city mentions from text',
    long_description=readme + '\n\n' + history,
    author='Denis Kovalev (fork from Yaser Martinez Palenzuela version)',
    author_email='aikikode@gmail.com',
    url='https://github.com/aikikode/geotext',
    packages=[
        'geotext',
    ],
    package_dir={'geotext': 'geotext', },
    include_package_data=True,
    package_data={'geotext': ['geotext/data/*.txt', ], },
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='geotext',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
