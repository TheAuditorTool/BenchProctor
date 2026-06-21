# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest72580(request: Request):
    auth_header = request.headers.get('authorization', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(auth_header).encode(), _parser)
    return {"updated": True}
