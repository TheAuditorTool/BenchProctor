# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest61841(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
