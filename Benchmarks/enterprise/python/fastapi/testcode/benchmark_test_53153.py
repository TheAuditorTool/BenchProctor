# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from lxml import etree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53153(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = FormData(payload=upload_name).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
