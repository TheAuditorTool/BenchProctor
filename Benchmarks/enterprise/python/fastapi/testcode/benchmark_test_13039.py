# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest13039(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    os.system('echo ' + str(data))
    return {"updated": True}
