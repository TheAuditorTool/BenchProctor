# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest12184(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
