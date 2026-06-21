# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest18925(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
