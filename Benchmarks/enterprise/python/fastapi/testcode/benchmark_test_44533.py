# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest44533(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = coalesce_blank(config_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
