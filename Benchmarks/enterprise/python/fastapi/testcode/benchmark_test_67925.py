# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest67925(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ctx = RequestContext(xml_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
