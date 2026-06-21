# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest44717():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
