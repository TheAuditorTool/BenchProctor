# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import asyncio


async def BenchmarkTest49348(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = await fetch_payload()
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
