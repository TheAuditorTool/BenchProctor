# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import importlib


async def BenchmarkTest03802(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
