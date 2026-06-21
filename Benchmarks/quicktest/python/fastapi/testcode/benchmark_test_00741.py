# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest00741(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
