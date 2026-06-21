# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def ensure_str(value):
    return str(value)

async def BenchmarkTest01431(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
