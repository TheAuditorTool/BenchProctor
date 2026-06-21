# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import urllib.request


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest57879(request: Request, req: UserInput):
    json_value = req.payload
    data = (lambda v: v.strip())(json_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
