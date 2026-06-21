# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest20178(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(header_value).encode(), _parser)
    return {"updated": True}
