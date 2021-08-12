import os
from setuptools import setup

DIR=os.path.dirname(__file__)

setup(
    name='wordlist_maker',
    version='1.1.8',
    description='generates wordlist',
    long_description=open(os.path.join(DIR, 'README.md')).read(),
    author='8harifi',
    author_email='8harifi@gmail.com',
    url='https://github.com/8harifi/wordlist_maker',
    py_modules=['main'],
    entry_points={
        'console_scripts':
        ['wordlist_maker=main:main'],
    })
