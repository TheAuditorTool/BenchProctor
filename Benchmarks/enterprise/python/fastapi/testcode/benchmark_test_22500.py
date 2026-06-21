# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import defusedxml.ElementTree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest22500(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
