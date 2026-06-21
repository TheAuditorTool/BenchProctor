# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import asyncio


async def BenchmarkTest65412(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return {"updated": True}
