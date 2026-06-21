# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest20735(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
