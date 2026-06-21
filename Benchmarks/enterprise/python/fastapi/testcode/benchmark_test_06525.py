# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import defusedxml.ElementTree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest06525(request: Request, req: UserInput):
    json_value = req.payload
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
