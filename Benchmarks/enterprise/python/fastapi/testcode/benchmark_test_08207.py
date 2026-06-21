# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest08207(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
