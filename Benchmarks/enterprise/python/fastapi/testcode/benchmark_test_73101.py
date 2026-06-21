# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest73101(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'w') as fh:
        fh.write('data')
    return {"updated": True}
