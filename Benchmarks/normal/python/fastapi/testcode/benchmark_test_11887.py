# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest11887(request: Request):
    upload_name = (await request.form()).get('upload', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(upload_name).encode(), _parser)
    return {"updated": True}
