# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import urllib.request


class UserInput(BaseModel):
    payload: str = ''
def coalesce_blank(value):
    return value or ''

async def BenchmarkTest54427(request: Request, req: UserInput):
    json_value = req.payload
    data = coalesce_blank(json_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
