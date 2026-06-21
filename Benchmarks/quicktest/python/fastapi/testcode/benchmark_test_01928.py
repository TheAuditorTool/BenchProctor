# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from lxml import etree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest01928(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
