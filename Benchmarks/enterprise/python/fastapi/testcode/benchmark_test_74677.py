# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest74677(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
