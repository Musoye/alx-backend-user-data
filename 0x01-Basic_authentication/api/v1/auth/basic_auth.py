#!/usr/bin/env python3
"""Basic Auth using AUTH"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic Authentication"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extrat base64 authorization"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """decode base63 authorization"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            bas = base64_authorization_header.encode('utf-8')
            return base64.b64decode(bas).decode('utf-8')
        except BaseException:
            return None
