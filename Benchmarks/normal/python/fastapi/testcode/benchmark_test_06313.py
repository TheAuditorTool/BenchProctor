# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import defusedxml.ElementTree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest06313(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
