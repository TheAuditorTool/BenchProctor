# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest30366(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % (json_value,)
    result = 100 / int(str(data))
    return {"updated": True}
