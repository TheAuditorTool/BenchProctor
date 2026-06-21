# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest74443(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
