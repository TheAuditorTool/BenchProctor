# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest70033(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    Fernet(cookie_value.encode() if isinstance(cookie_value, str) else cookie_value).encrypt(b'data')
    return {"updated": True}
