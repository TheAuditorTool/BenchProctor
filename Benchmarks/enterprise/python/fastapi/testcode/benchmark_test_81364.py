# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest81364(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
