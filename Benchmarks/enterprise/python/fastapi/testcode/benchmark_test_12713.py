# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest12713(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    Fernet(secret_value.encode() if isinstance(secret_value, str) else secret_value).encrypt(b'data')
    return {"updated": True}
