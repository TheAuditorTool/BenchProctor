# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest69320(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    globals()['counter'] = int(data)
    return {"updated": True}
