# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from lxml import etree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest05163(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
