# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def relay_value(value):
    return value

async def BenchmarkTest06646(request: Request):
    path_value = request.path_params.get('id', '')
    data = relay_value(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
