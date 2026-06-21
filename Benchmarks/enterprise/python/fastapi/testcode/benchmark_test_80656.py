# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest80656(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = '%s' % (secret_value,)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
