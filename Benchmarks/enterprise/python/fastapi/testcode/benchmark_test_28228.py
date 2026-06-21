# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest28228(request: Request):
    user_id = request.query_params.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
