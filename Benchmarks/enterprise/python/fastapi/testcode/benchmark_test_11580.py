# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest11580(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = '%s' % str(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
