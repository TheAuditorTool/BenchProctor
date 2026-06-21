# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from fastapi import Form
import os


request_state: dict[str, str] = {}

async def BenchmarkTest61880(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
