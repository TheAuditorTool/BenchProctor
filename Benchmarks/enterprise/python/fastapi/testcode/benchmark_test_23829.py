# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest23829(request: Request, req: UserInput):
    json_value = req.payload
    ctx = RequestContext(json_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
