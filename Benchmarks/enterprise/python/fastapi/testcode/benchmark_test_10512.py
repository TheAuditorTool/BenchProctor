# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from lxml import etree


async def BenchmarkTest10512(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
