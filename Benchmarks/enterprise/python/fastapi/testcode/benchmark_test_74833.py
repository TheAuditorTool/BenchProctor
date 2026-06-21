# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest74833(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = coalesce_blank(raw_body)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
