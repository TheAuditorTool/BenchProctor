# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import subprocess


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest49507(request: Request, req: UserInput):
    json_value = req.payload
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
