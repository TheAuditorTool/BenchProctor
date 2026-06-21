# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest38447(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
