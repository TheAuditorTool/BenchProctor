# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest00423(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
