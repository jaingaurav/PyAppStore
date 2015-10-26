#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyappstore',
    version='0.1.0',
    description=": Command line tools to install from the App Store",
    long_description=readme + '\n\n' + history,
    author="Gaurav Jain",
    author_email='gaurav@gauravjain.org',
    url='https://github.com/jaingaurav/pyappstore',
    packages=[
        'pyappstore',
    ],
    package_dir={'pyappstore':
                 'pyappstore'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pyappstore',
    entry_points={
        'console_scripts': [
            'pyappstore = pyappstore.pyappstore:_main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
