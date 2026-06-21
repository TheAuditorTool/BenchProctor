# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import importlib


async def BenchmarkTest10711(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    async def _evasion_task():
        importlib.import_module(str(data))
    await _evasion_task()
    return {"updated": True}
