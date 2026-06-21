# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


request_state: dict[str, str] = {}

async def BenchmarkTest05882(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
