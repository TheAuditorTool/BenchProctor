# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest35791(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
