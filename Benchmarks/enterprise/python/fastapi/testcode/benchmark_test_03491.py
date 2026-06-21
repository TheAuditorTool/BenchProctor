# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
import asyncio


async def BenchmarkTest03491(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    yaml.safe_load(data)
    return {"updated": True}
