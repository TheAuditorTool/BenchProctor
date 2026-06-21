# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest75067(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
