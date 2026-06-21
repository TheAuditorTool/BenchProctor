# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from lxml import etree


async def BenchmarkTest52752(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
