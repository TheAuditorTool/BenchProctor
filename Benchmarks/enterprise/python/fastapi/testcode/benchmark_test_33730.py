# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest33730(request: Request):
    referer_value = request.headers.get('referer', '')
    Fernet(referer_value.encode() if isinstance(referer_value, str) else referer_value).encrypt(b'data')
    return {"updated": True}
