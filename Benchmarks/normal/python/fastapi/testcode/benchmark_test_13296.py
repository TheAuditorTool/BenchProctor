# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest13296(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
