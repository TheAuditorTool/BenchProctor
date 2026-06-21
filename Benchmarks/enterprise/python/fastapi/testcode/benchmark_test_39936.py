# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from cryptography.fernet import Fernet
import asyncio


async def BenchmarkTest39936(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return prop_value
    data = await fetch_payload()
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return {"updated": True}
