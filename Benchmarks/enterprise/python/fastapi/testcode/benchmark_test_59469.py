# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest59469(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
