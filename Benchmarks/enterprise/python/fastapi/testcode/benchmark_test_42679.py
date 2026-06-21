# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import socket


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest42679(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return {"updated": True}
