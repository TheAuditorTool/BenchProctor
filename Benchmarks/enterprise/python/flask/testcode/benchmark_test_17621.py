# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from lxml import etree


def BenchmarkTest17621():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
