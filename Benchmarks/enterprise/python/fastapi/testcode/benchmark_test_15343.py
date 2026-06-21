# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest15343(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = coalesce_blank(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
