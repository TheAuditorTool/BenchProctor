# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest05354(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
