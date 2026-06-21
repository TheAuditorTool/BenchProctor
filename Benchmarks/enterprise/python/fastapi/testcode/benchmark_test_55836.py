# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest55836(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
