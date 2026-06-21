# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest56399(request: Request):
    query_array = request.query_params.get('items', '')
    ctx = RequestContext(query_array)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return {"updated": True}
