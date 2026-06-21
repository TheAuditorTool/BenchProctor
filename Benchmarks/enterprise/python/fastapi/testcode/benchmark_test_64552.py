# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from lxml import etree


async def BenchmarkTest64552(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
