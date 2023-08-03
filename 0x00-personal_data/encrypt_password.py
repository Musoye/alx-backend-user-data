#!/usr/bin/env python3
"""encryption of password"""


import bcrypt


def hash_password(password: str):
    """Hashing of Passsowrd"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
