# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest01957(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % (config_value,)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
