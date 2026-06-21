# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest41214(request: Request, req: UserInput):
    json_value = req.payload
    data, _sep, _rest = str(json_value).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
