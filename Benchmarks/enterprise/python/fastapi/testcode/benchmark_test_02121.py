# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import asyncio


async def BenchmarkTest02121(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = await fetch_payload()
    yaml.safe_load(data)
    return {"updated": True}
