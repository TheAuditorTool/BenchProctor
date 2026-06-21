# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


request_state: dict[str, str] = {}

async def BenchmarkTest03024(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
