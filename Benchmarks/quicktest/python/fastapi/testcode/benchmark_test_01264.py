# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from lxml import etree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest01264(request: Request, req: UserInput):
    json_value = req.payload
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
