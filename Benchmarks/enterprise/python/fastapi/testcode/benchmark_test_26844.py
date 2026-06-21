# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile


def normalise_input(value):
    return value.strip()

async def BenchmarkTest26844(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = normalise_input(raw_body)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
