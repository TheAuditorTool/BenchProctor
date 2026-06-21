# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest13281(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(multipart_value).encode(), _parser)
    return {"updated": True}
