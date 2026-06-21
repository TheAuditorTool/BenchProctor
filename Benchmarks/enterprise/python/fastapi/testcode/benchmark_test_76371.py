# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest76371(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
