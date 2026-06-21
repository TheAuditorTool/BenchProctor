# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def to_text(value):
    return str(value).strip()

async def BenchmarkTest33440(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
