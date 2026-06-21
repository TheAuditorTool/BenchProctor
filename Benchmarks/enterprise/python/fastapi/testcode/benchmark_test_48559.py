# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest48559(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = coalesce_blank(auth_header)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return {"updated": True}
