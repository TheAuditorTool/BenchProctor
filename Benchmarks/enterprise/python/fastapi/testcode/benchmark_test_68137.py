# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import subprocess


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest68137(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
