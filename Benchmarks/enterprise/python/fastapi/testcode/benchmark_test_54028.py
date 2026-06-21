# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
from lxml import etree


async def BenchmarkTest54028(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return {"updated": True}
