try:
    import setuptools
except ImportError:
    pass
from distutils.core import setup
from glob import glob
import os
import sys

#html_docs = glob('dbf/html/*')

long_desc="""
Currently supports dBase III, Clipper, FoxPro, and Visual FoxPro tables. Text is returned as unicode, and codepage settings in tables are honored. Memos and Null fields are supported.  Documentation needs work, but author is very responsive to e-mails.

Not supported: index files (but can create tempory non-file indexes), auto-incrementing fields, and Varchar fields.

Installation:  `pip install dbf`

There may be messages about byte-compiling failures -- you can safely ignore them (this is a multi-version release, and 2 and 3 don't like some of each other's code).
"""

if sys.version_info[:2] < (3, 4):
    requirements = ['enum34']
else:
    requirements = []

py2_only = ('dbf/ver_2.py', )
py3_only = ('dbf/ver_32.py', 'dbf/ver_33.py')
make = []

data = dict(
        name='dbf',
        version='0.96.8',
        license='BSD License',
        description='Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf files (including memos)',
        long_description=long_desc,
        url='https://pypi.python.org/pypi/dbf',
        packages=['dbf', ],
        provides=['dbf'],
        install_requires=['aenum'],
        author='Ethan Furman',
        author_email='ethan@stoneleaf.us',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Database',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            ],
        )

if __name__ == '__main__':
    setup(**data)

