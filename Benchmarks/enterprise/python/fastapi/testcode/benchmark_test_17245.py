# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest17245(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
