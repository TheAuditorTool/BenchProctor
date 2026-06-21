# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import asyncio


async def BenchmarkTest02205(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    yaml.safe_load(data)
    return {"updated": True}
