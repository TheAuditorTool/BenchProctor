# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
from pydantic import BaseModel
import subprocess


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest11471(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
