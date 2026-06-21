# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest02508(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
