# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
import socket


async def BenchmarkTest81163(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    def _primary():
        s = socket.create_connection((str(data), 80))
        s.close()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
