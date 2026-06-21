# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest12625(request: Request):
    host_value = request.headers.get('host', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(host_value).encode(), _parser)
    return {"updated": True}
