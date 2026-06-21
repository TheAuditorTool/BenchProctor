# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import requests


async def BenchmarkTest51776(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
