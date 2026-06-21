# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest44486(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
