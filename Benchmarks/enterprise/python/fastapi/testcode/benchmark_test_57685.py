# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest57685(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = coalesce_blank(auth_header)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
