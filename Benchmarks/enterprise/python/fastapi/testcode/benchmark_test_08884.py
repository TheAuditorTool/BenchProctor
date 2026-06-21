# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest08884(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
