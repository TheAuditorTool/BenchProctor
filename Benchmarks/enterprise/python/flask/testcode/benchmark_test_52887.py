# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest52887():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
