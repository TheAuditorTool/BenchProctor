# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
import defusedxml.ElementTree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest63976(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
