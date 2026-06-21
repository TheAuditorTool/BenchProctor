# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import importlib


async def BenchmarkTest67661(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
