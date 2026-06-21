# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest36898(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = FormData(payload=file_value).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
