# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from lxml import etree


async def BenchmarkTest39101(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return {"updated": True}
