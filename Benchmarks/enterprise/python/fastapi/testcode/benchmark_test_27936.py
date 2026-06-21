# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from lxml import etree


async def BenchmarkTest27936(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
