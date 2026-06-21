# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest50893(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ctx = RequestContext(ua_value)
    data = ctx.payload
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
