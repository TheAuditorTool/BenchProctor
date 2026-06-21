# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


request_state: dict[str, str] = {}

async def BenchmarkTest53141(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
