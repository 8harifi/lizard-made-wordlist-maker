import os
from setuptools import setup

DIR=os.path.dirname(__file__)

setup(
    name='lizard-made-wordlist-maker',
    version='1.1.1',
    description='generates wordlist',
    long_description=open(os.path.join(DIR, 'README.md')).read(),
    author='the-liz4rd',
    author_email='oliver.the.lizard@yandex.com',
    url='https://github.com/the-liz4rd/lizard-made-wordlist-maker',
    py_modules=['main'],
    entry_points={
        'console_scripts':
        ['wordlist_maker=main:main'],
    })
