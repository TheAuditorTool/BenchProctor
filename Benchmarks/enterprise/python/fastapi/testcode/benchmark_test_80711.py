# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from lxml import etree


async def BenchmarkTest80711(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
