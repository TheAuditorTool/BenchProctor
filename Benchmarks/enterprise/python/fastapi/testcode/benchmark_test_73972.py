# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest73972(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
