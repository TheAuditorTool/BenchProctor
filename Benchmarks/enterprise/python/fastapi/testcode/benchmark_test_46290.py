# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest46290(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '{}'.format(header_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
