# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from fastapi import Form


async def BenchmarkTest29392(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
