# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet


async def BenchmarkTest60877(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(prop_value)
    data = collected
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
