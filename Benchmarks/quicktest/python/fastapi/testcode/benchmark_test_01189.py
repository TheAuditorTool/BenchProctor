# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest01189(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
