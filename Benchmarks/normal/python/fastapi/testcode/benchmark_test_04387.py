# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from lxml import etree


async def BenchmarkTest04387(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
