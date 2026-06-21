# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest64662(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
