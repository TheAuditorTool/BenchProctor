# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest35773(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
