# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import defusedxml.ElementTree


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest49887(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
