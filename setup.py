#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Flask-Error
-----------
What is this?
    Flask-Error provides JSON outputs when exceptions are raised.

Why this extension?
    Because writing error when the exceptions are raised
        is very board as you know.
    This extension may reduce your coding time; you don't need
    to point whatever errors inheriting BaseException
    (The base class of Built-in Exceptions)!
    Besides, you can defined your custom errors and raise it!.

LICENSE
Flask-Error
Copyright (C) 2014  Hiroaki Yamamoto

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


from setuptools import setup
from flask_error import (__version__,
                         __author__,
                         __license__,
                         __url__)

setup(
    name="Flask-Error",
    version=__version__,
    url=__url__,
    author=__author__["name"],
    author_email=__author__["email"],
    description="Automatic error handler blueprints for Flask",
    license=__license__,
    py_modules=["flask_error"],
    install_requires=["Flask"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ])
