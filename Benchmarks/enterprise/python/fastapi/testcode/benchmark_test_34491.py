# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest34491(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return {"updated": True}
