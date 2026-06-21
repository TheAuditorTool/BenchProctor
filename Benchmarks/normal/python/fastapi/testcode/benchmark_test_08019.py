# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def ensure_str(value):
    return str(value)

async def BenchmarkTest08019(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
