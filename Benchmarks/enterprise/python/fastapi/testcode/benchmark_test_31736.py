# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from urllib.parse import unquote


async def BenchmarkTest31736(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
