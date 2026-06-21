# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


async def BenchmarkTest15739(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
