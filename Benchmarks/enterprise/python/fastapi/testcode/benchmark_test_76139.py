# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest76139(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
