# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
request_state: dict[str, str] = {}

async def BenchmarkTest77180(request: Request, req: UserInput):
    json_value = req.payload
    request_state['last_input'] = json_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
