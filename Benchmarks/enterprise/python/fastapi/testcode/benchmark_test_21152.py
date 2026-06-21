# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest21152(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
