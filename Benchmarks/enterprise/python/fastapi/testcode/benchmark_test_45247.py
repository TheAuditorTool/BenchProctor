# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio


async def BenchmarkTest45247(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return config_value
    data = await fetch_payload()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
