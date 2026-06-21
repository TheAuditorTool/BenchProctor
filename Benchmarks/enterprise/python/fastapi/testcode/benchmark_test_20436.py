# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest20436(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
