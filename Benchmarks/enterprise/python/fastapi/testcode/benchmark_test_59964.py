# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest59964(request: Request):
    origin_value = request.headers.get('origin', '')
    Fernet(origin_value.encode() if isinstance(origin_value, str) else origin_value).encrypt(b'data')
    return {"updated": True}
