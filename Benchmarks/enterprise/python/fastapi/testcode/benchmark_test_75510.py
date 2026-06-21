# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
import importlib


async def BenchmarkTest75510(request: Request):
    origin_value = request.headers.get('origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return {"updated": True}
