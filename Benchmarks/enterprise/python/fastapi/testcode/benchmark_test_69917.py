# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import asyncio
import urllib.request
import urllib.parse
import ssl


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest69917(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}
