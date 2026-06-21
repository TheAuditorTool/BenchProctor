# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest78609(request: Request):
    auth_header = request.headers.get('authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
