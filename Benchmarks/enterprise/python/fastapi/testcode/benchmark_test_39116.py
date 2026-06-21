# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


request_state: dict[str, str] = {}

async def BenchmarkTest39116(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
