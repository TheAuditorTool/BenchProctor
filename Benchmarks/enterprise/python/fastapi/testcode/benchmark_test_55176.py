# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import importlib


async def BenchmarkTest55176(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
