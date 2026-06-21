# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest21497(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    Fernet(secret_value.encode() if isinstance(secret_value, str) else secret_value).encrypt(b'data')
    return {"updated": True}
