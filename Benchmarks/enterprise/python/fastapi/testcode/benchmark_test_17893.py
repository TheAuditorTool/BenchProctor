# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def coalesce_blank(value):
    return value or ''

async def BenchmarkTest17893(request: Request, req: UserInput):
    json_value = req.payload
    data = coalesce_blank(json_value)
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    await _evasion_task()
    return {"updated": True}
