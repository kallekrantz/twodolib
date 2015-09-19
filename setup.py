#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script for twodolib."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'wheel',
]

test_requirements = [
    'tox',
]

setup(
    name='twodolib',
    version='0.0.1',
    description="Functions to manage the 2DoApp from the command line.",
    long_description=readme + '\n\n' + history,
    author="Karsten Schulz",
    author_email='github@karstenschulz.biz',
    url='https://github.com/KarstenSchulz/twodolib',
    packages=[
        'twodolib',
    ],
    package_dir={'twodolib': 'twodolib'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'task2do = twodolib.cli:main'
        ]
    },
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='twodolib',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: MacOS :: MacOS X',
        'Natural Language :: English',
        'Topic :: Productivity',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
