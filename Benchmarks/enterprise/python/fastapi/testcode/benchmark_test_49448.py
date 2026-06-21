# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest49448(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
