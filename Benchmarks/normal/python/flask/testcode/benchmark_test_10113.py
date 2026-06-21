# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from lxml import etree


def ensure_str(value):
    return str(value)

def BenchmarkTest10113():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    async def _evasion_task():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
