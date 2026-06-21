# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest75159(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    os.remove(str(data))
    return {"updated": True}
