# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


async def BenchmarkTest61348(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
