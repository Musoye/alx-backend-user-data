#!/usr/bin/env python3
"""Aythentication method definition"""
from flask import request
from typing import TypeVar, List


class Auth:
    """Authentication class definition"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require of authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """The authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """The Crrent User"""
        return None
