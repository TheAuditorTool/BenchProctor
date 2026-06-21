# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import asyncio


async def BenchmarkTest64269(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
