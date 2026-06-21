# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def relay_value(value):
    return value

async def BenchmarkTest11086(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    await _evasion_task()
    return {"updated": True}
