# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


request_state: dict[str, str] = {}

async def BenchmarkTest42366(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
