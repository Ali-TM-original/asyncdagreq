"""
Asyncdagpi
~~~~~~~~~~~~~~~~~~~
An async wrapper for dagpi
:copyright: (c) 2020 Ali-TM-original
:license: MIT, see LICENSE for more details.
"""

from collections import namedtuple

__title__ = "asyncdagreq"
__author__ = "Ali-TM-original"
__license__ = "MIT"
__copyright__ = "Copyright 2020 Daggy1234"
__version__ = '1.1.7'

from .Client import Asyncdagreq
from .Errors import *

VersionInfo = namedtuple('VersionInfo',
                         'major minor micro releaselevel serial')

version_info = VersionInfo(major=3, minor=3, micro=2, releaselevel='unstable',
                           serial=0)
