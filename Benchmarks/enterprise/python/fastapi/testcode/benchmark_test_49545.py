# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import asyncio


async def BenchmarkTest49545(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = await fetch_payload()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
