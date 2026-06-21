# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest22373(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    await _evasion_task()
    return {"updated": True}
