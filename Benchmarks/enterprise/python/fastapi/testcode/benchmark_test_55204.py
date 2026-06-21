# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest55204(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
