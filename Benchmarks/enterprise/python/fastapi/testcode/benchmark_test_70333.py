# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest70333(request: Request):
    host_value = request.headers.get('host', '')
    Fernet(host_value.encode() if isinstance(host_value, str) else host_value).encrypt(b'data')
    return {"updated": True}
