# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from lxml import etree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest45378(request: Request, req: UserInput):
    json_value = req.payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(json_value).encode(), _parser)
    return {"updated": True}
