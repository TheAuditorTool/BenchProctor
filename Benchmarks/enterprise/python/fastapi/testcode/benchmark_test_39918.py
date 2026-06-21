# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


request_state: dict[str, str] = {}

async def BenchmarkTest39918(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
