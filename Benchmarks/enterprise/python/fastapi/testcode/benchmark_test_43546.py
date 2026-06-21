# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


async def BenchmarkTest43546(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
