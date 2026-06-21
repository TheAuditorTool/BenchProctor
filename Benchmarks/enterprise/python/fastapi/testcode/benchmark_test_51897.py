# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
import importlib


async def BenchmarkTest51897(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
