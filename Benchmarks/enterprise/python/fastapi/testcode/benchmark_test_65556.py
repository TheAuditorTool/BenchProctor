# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import subprocess


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest65556(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
