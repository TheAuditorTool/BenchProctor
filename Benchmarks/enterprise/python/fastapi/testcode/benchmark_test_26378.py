# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest26378(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % (forwarded_ip,)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
