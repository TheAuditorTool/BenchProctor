# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest23799(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
