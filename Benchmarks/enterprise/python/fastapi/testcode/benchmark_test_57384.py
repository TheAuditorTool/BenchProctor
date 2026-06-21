# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest57384(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    result = 100 / int(str(data))
    return {"updated": True}
