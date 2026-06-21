# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest42074(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
