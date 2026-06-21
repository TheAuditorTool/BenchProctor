# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04877(request: Request, req: UserInput):
    json_value = req.payload
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
