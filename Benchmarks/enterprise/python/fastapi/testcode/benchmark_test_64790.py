# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


request_state: dict[str, str] = {}

async def BenchmarkTest64790(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
