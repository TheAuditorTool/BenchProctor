# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio


async def BenchmarkTest75593(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = await fetch_payload()
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
