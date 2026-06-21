# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest02512(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
