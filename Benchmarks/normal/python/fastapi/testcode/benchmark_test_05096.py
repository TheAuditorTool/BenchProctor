# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import asyncio
from lxml import etree


async def BenchmarkTest05096(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = await fetch_payload()
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    await _evasion_task()
    return {"updated": True}
