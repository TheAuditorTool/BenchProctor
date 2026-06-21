# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
import defusedxml.ElementTree


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest59422(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
