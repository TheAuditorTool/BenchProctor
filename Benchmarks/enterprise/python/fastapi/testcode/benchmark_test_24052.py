# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
import asyncio


async def BenchmarkTest24052(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
