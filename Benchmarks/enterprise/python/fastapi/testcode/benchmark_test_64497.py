# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


async def BenchmarkTest64497(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
