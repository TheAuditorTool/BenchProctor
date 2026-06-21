# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest06324(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
