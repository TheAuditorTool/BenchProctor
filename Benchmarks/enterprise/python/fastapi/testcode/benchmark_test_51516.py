# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest51516(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = normalise_input(multipart_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
