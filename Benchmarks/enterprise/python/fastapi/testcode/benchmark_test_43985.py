# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest43985(request: Request):
    referer_value = request.headers.get('referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
