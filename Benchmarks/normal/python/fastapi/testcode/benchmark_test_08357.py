# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import defusedxml.ElementTree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest08357(request: Request, req: UserInput):
    json_value = req.payload
    defusedxml.ElementTree.fromstring(str(json_value))
    return {"updated": True}
