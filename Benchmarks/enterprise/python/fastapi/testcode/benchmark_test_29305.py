# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest29305(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = coalesce_blank(auth_header)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
