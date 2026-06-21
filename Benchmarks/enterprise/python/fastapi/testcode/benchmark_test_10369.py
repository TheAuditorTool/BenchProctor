# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import subprocess


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest10369(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
