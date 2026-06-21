# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def relay_value(value):
    return value

async def BenchmarkTest40918(request: Request, req: UserInput):
    json_value = req.payload
    data = relay_value(json_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
