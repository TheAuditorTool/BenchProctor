# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest24538(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
