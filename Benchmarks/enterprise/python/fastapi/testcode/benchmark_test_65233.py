# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import asyncio


async def BenchmarkTest65233(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = await fetch_payload()
    processed = data[:64]
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return {"updated": True}
