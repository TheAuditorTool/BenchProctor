# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest34521(request: Request, req: UserInput):
    json_value = req.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(json_value)}, verify=True)
    return {"updated": True}
