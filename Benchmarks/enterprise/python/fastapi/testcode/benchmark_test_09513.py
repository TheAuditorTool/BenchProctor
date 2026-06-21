# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest09513(request: Request):
    host_value = request.headers.get('host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
