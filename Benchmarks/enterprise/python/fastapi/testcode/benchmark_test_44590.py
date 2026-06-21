# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest44590(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    os.remove(str(data))
    return {"updated": True}
