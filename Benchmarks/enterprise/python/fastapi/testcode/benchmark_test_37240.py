# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest37240(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    Fernet(config_value.encode() if isinstance(config_value, str) else config_value).encrypt(b'data')
    return {"updated": True}
