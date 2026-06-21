# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest55266(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
