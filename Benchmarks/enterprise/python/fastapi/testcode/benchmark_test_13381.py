# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import asyncio


async def BenchmarkTest13381(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    eval(compile('_resp = requests.get(str(data))\nexec(_resp.text)', '<sink>', 'exec'))
    return {"updated": True}
