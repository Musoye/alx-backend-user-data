#!/usr/bin/env python3
"""Authentication models"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication function"""

    def require_auth(self, path: str, excluded_paths: List[str] = None) -> bool:
        """Require path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Require header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
