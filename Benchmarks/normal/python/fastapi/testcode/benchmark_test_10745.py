# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest10745(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
