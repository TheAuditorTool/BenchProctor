# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest75702(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = '%s' % (secret_value,)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
