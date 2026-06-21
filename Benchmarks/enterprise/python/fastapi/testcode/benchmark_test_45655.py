# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


async def BenchmarkTest45655(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
