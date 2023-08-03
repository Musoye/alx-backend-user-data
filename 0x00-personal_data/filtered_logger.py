#!/usr/bin/env python3
"""Deal about filtering data"""

from typing import List
import logging
import re
from os import getenv
import mysql.connector


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''
    function called filter_datum that
    returns the log message obfuscated
    '''
    for field in fields:
        mes = re.sub(field+'=.*?'+separator,
                     field+'='+redaction+separator, message)
    return mes
