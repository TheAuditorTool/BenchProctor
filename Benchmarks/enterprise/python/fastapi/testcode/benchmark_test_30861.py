# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest30861(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
