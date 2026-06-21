# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest38346(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(raw_body).encode(), _parser)
    return {"updated": True}
