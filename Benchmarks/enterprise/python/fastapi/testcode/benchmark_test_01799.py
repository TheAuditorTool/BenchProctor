# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from lxml import etree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01799(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
