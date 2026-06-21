# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import urllib.request


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest00475(request: Request, req: UserInput):
    json_value = req.payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(json_value)).read()
    return {"updated": True}
