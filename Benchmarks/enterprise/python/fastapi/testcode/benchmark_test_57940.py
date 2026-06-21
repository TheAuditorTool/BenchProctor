# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from urllib.parse import unquote
import os


async def BenchmarkTest57940(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
