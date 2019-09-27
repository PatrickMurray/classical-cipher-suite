#!/usr/bin/env python3


import setuptools


with open('README.md') as handler:
    readme_markdown = handler.read()
    
    setuptools.setup(
        name='Classical Cipher Suite',
        version='0.0.1',
        author='Patrick Murray',
        author_email='patrick@murray.systems',
        description='A collection of neat historical ciphers and tooling to use them for fun and profit.',
        long_description=readme_markdown,
	long_description_content_type='text/markdown',
	url='https://github.com/PatrickMurray/classical-cipher-suite',
	packages=setuptools.find_packages()
    )
