# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest17869(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
