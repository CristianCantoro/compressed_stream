#!/usr/bin/env python3
"""compressed_stream
   -----------------
   A simple python module to handle streams of compressed files.

"""

from setuptools import setup, find_packages

setup(
    name='compressed_stream',
    version='0.0.2',
    author='Cristian Consonni',
    author_email='crist' 'ian' '<dot>' 'conson' 'ni' '<a' 't>' 'uni' 'tn' '<d' 'ot>i' 't',
    license='MIT',
    description='Handle streams of compressed files.',
    long_description=__doc__,
    url='https://github.com/CristianCantoro/compressed_stream',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'decompressgrep=compressed_stream.__main__:decompressgrep',
            'decompressless=compressed_stream.__main__:decompressless',
            'decompressmore=compressed_stream.__main__:decompressmore',
            'decompressdiff=compressed_stream.__main__:decompressdiff',
            'decompresscmp=compressed_stream.__main__:decompresscmp',
            'decompresscat=compressed_stream.__main__:decompresscat',
        ],
    },
    options={
        'build_scripts': {
            'executable': 'python3',
        },
    },
    install_requires=[],
    zip_safe=False,
)
