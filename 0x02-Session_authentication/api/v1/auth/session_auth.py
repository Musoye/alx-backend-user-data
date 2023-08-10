#!/usr/bin/env python3
"""Session authentication"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create session"""
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        key = str(uuid4())
        SessionAuth.user_id_by_session_id[key] = user_id
        return user_id  
