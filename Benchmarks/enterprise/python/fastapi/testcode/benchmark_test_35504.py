# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest35504(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = f'{secret_value:.200s}'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
