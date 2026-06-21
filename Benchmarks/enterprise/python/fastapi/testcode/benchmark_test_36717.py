# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import importlib
import sys


async def BenchmarkTest36717(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
