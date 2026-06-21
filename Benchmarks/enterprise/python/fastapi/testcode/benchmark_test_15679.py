# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest15679(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    async def _evasion_task():
        os.system('echo ' + str(data))
    await _evasion_task()
    return {"updated": True}
