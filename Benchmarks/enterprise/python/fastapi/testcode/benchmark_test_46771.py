# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest46771(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
