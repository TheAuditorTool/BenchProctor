# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest37223(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    os.system('echo ' + str(data))
    return {"updated": True}
