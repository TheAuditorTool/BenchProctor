# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


async def BenchmarkTest66951(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
