# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest03164(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
