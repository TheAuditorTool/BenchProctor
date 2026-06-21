# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from lxml import etree


def BenchmarkTest30733():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
