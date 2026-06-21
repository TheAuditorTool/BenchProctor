# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from lxml import etree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest43691(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
