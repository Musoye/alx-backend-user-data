#!/usr/bin/env python3
"""Authentication models"""


from flask import request
from typing import TypeVar


class Auth:
    """authentication function"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require path"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """require header"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
