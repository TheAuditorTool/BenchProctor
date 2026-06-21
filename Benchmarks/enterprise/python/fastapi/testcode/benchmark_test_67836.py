# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import asyncio


async def BenchmarkTest67836(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    yaml.safe_load(data)
    return {"updated": True}
