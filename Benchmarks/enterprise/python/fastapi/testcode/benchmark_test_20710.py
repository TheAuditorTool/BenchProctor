# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest20710(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
