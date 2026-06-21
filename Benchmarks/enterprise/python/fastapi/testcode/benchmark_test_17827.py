# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import requests


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest17827(request: Request, req: UserInput):
    json_value = req.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(json_value)}, verify=False)
    return {"updated": True}
