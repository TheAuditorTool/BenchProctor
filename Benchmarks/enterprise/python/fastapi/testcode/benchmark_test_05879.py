# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from lxml import etree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest05879(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
