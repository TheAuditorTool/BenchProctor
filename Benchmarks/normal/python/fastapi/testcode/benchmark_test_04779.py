# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest04779(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = FormData(payload=secret_value).payload
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
