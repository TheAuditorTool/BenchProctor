# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import requests


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest03202(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
