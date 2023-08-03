#!/usr/bin/env python3
"""encryption of password"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Hashing of Passsowrd"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
