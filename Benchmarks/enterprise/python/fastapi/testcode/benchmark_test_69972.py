# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from fastapi import Form
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest69972(request: Request, field: str = Form('')):
    field_value = field
    ctx = RequestContext(field_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
