# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest18603(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
