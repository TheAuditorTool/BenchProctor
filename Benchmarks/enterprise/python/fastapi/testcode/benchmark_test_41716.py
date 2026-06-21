# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest41716(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
