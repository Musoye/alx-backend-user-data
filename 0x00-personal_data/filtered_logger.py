#!/usr/bin/env python3
"""Deal about filtering data"""

from typing import List
import logging
import re
from os import getenv
import mysql.connector


PII_FIELDS = ('email', 'name', 'ssn', 'password', 'phone')


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        '''
        format method to filter values in
        incoming log records using filter_datum
        '''
        message = super(RedactingFormatter, self).format(record)
        redact = filter_datum(self.fields, self.REDACTION,
                              message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    '''get logging function'''
    logger = logging.getLogger("user_data")
    logger.propagate = False
    logger.setLevel(logging.INFO)
    handler = logger.StreamHandler()
    fmt = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    return logger
