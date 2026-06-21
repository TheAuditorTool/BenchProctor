# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest72066(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
