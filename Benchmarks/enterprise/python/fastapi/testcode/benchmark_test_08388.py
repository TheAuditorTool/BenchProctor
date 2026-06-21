# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from lxml import etree


async def BenchmarkTest08388(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
