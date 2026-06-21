# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest50164(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
