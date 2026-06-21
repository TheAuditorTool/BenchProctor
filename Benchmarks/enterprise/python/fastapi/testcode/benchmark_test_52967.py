# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest52967(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
