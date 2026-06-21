# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest38837(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
