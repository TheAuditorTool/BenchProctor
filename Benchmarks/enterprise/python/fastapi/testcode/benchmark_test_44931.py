# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


request_state: dict[str, str] = {}

async def BenchmarkTest44931(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
