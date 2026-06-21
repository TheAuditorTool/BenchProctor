# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import asyncio


async def BenchmarkTest66885(request: Request):
    auth_header = request.headers.get('authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = await fetch_payload()
    processed = data[:64]
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return {"updated": True}
