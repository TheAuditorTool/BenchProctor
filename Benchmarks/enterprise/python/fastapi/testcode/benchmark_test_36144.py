# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest36144(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
