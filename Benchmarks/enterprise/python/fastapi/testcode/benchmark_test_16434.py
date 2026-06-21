# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest16434(request: Request, req: UserInput):
    json_value = req.payload
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
