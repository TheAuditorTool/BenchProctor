# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest10774(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
