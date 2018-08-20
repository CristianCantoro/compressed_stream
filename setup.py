"""compressed_stream
   -----------------
   A simple python module to handle streams of compressed files.

"""

from setuptools import setup, find_packages

setup(
    name='compressed_stream',
    version='0.0.1',
    author='Cristian Consonni',
    author_email='crist' 'ian' '<dot>' 'conson' 'ni' '<a' 't>' 'uni' 'tn' '<d' 'ot>i' 't',
    license='MIT',
    description='Handle streams of compressed files.',
    long_description=__doc__,
    url='https://github.com/CristianCantoro/compressed_stream',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'decompresscat=compressed_stream.__main__:main',
        ],
    },
    install_requires=[],
)
