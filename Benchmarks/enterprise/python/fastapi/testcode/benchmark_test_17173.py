# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from pydantic import BaseModel
import urllib.request
import urllib.parse
import ssl


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest17173(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
