# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest55540(request: Request):
    origin_value = request.headers.get('origin', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(origin_value).encode(), _parser)
    return {"updated": True}
