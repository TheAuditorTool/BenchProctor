# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import time
from lxml import etree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest42263(request: Request, req: UserInput):
    json_value = req.payload
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
