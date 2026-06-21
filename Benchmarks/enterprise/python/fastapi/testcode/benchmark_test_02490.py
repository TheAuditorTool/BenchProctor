# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
import importlib
import sys


async def BenchmarkTest02490(request: Request):
    ua_value = request.headers.get('user-agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
