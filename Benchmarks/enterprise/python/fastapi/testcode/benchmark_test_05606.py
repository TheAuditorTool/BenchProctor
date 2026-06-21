# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


async def BenchmarkTest05606(request: Request):
    path_value = request.path_params.get('id', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(path_value))
    os.chmod(path, 0o777)
    return {"updated": True}
