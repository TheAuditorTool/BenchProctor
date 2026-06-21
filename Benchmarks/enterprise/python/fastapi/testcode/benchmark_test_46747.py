# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest46747(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
