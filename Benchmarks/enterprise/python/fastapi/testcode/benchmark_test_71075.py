# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


request_state: dict[str, str] = {}

async def BenchmarkTest71075(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    await _evasion_task()
    return {"updated": True}
